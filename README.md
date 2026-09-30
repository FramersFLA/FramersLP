# Framers Linguistic Protocol

Freedom through clarity. Static, multi-page GitHub Pages website.

## Publish on GitHub Pages

In **Settings → Pages → Build and deployment**, select **Deploy from a branch**, branch **main**, folder **/docs**, then Save. Merge the reviewed rebuild into main to publish. The expected project URL is https://framersfla.github.io/FramersLP/.

`docs/index.html` is the entry point. All pages, styles, scripts, and the PDF are in `docs`; relative URLs preserve the `/FramersLP/` project prefix. `docs/.nojekyll` disables Jekyll processing. No server-side runtime, package installation, custom domain, or build step is required on GitHub Pages.

Verified in GitHub Settings → Pages on September 30, 2026: publishing source is already **main /docs**, with HTTPS enforced. The review branch does not publish until merged.

## Structure and editing

- `site/template.html`: shared document shell.
- `site/partials/`: one shared header/navigation and footer source.
- `site/content/`: Home, About, FAQ, Contact, Protocol, and legacy email-help content.
- `docs/`: committed publishing output, stylesheet, script, and PDF.
- `scripts/build_site.py`: standard-library-only generator.
- `scripts/check_site.py`: validates case-sensitive local links, fragments, shared navigation, entry point, and PDF signature.
- `scripts/build_whitepaper.py`: optional PDF regeneration; requires ReportLab.
- `Website`: preserved legacy bundled source; not the publishing entry point.

After editing page content or partials:

```sh
python scripts/build_site.py
python scripts/check_site.py
```

Commit both sources and generated HTML. For a local preview:

```sh
python -m http.server 8000 --directory docs
```

## Email forms

FAQ and Contact prepare `mailto:` drafts for the existing repository contact, `foundersfla@gmail.com`. Visitors must review and send them in a configured email app. There is no backend, message storage, or automatic sending. A direct email link remains available without JavaScript. The legacy `thanks.html` URL explains this flow and never claims a message was received.

## White paper status

The original `docs/FLP_Whitepaper.pdf` was plain placeholder text, and the home page linked to a different capitalization. The new valid PDF is explicitly a **reconstructed draft overview, pending founder review**, based on existing repository material. It is not the original full white paper. Replace it with the approved document at the same exact-case filename when available. Home and Protocol use a `download` link.

## License

The existing [GPL-3.0 license](docs/LICENSE) is retained.
