# Aurealm Hugo Theme

A Hugo theme derived from [Luke Smith's simple Hugo theme 'lugo'](https://github.com/LukeSmithxyz/lugo) designed for the Aurealm Pen & Paper website.

## Getting Started

```sh
hugo new site new-site
cd new-site
git clone https://github.com/MiragonMx/aurealm_theme themes/aurealm
echo "theme = 'aurealm'" >> config.toml
# Or, if the Hugo version is > 0.110.0
# echo "theme = 'aurealm'" >> hugo.toml
cp themes/aurealm/static/style.css static/
```

## Notes (same as for lugo)

- Makes one RSS feed for the entire site at `/index.xml`
- Stylesheet is in `/style.css` and includes some important stuff for partials.
- If a post is tagged, links to the tags are placed at the bottom of the post.
- `nextprev.html` adds links to the Next and Previous articles to the bottom of a page.
- `taglist.html` links all tags an article is tagged to for related content.
