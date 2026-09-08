#!/usr/bin/env python3
"""Developer-only backdrop diagnostic using a disposable Marionette profile."""

import argparse
import json
from pathlib import Path
import tempfile

from marionette_driver.marionette import Marionette


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--binary', default='/Applications/Zen.app/Contents/MacOS/zen')
    parser.add_argument('--port', type=int, default=2833)
    parser.add_argument('--disable-native-compositor', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    prefs = {'zen.welcome-screen.seen': True}
    if args.disable_native_compositor:
        prefs['gfx.webrender.compositor'] = False
    browser = Marionette(
        bin=args.binary, headless=False, port=args.port,
        app_args=['--remote-allow-system-access'], prefs=prefs,
        gecko_log=str(Path(tempfile.gettempdir()) / 'zen-find-glass.log'),
    )
    try:
        browser.start_session()
        browser.navigate((root / 'tests/glass-comparison.html').as_uri())
        browser.set_context('chrome')
        result = browser.execute_async_script('''
          const done = arguments[arguments.length - 1];
          (async () => {
            const style = document.createElement('style');
            style.textContent = arguments[0];
            document.documentElement.append(style);
            const bar = await gBrowser.getFindBar();
            bar.open();
            bar._findField.value = 'DIAG-PAGE';
            bar.style.setProperty('--mod-zen-find-background-opacity', '.4');
            bar.style.setProperty('--mod-zen-find-background-color', '#ffffff');
            const properties = ['display', 'position', 'z-index', 'opacity',
              'filter', 'backdrop-filter', 'clip-path', 'mask-image', 'isolation',
              'mix-blend-mode', 'contain', 'container-type', 'will-change',
              'transform', 'overflow', 'view-transition-name'];
            const ancestors = [];
            for (let element = bar; element; element = element.parentElement) {
              const computed = getComputedStyle(element);
              ancestors.push({tag: element.tagName, id: element.id,
                classes: element.className,
                css: Object.fromEntries(properties.map(property =>
                  [property, computed.getPropertyValue(property)]))});
            }
            done({version: Services.appinfo.version,
              buildID: Services.appinfo.appBuildID,
              remote: gBrowser.selectedBrowser.isRemoteBrowser,
              nativeCompositorPref: Services.prefs.getBoolPref('gfx.webrender.compositor'),
              gfx: Cc['@mozilla.org/gfx/info;1'].getService(Ci.nsIGfxInfo).getFeatures(),
              ancestors});
          })().catch(error => done({error: String(error)}));
        ''', script_args=[(root / 'chrome.css').read_text()])
        print(json.dumps(result, indent=2), flush=True)
        if 'error' in result:
            raise RuntimeError(result['error'])
        print('Verify DIAG-PAGE in an OS screenshot, including the page B panel.')
        input('Press Enter for a same-document chrome background: ')
        browser.execute_script('''
          const bar = document.querySelector('findbar');
          const stripes = document.createElementNS('http://www.w3.org/1999/xhtml', 'div');
          stripes.id = 'zen-find-diagnostic-stripes';
          stripes.textContent = 'CHROME BACKGROUND 0123456789 '.repeat(12);
          stripes.style.cssText = 'position:absolute;grid-area:browserstack;' +
            'inset:0 0 auto;height:160px;overflow:hidden;z-index:9;' +
            'background:repeating-linear-gradient(90deg,#ee6175 0 32px,' +
            '#65c2cd 32px 64px,#f3d86a 64px 96px,white 96px 128px);' +
            'font:bold 32px monospace;color:black;';
          bar.before(stripes);
          bar._findField.value = 'DIAG-CHROME';
        ''')
        input('Verify DIAG-CHROME, then press Enter for a direct filter over the page: ')
        browser.execute_script('''
          document.getElementById('zen-find-diagnostic-stripes').remove();
          const style = document.createElement('style');
          style.textContent = 'findbar{backdrop-filter:blur(24px)!important;' +
            'background:#ffffff66!important;transform:none!important;' +
            'left:150px!important;container-type:normal!important;contain:none!important}' +
            'findbar::before{content:none!important}';
          document.documentElement.append(style);
          document.querySelector('findbar')._findField.value = 'DIAG-DIRECT';
        ''')
        input('Verify DIAG-DIRECT, then press Enter to close the disposable browser: ')
    finally:
        try:
            if browser.session:
                browser.quit()
        finally:
            browser.cleanup()


if __name__ == '__main__':
    main()
