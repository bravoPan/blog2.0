from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

register = template.Library()

class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang=None):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                   mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):
    high_light_render = HighlightRenderer()
    markdown = mistune.Markdown(renderer=high_light_render)
    result = force_text(value)
    return mark_safe(markdown(result))
