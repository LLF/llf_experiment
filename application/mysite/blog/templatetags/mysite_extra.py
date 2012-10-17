from django import template
import datetime

register = template.Library()

@register.tag(name = 'mysite')
def tag_test(parse, token):
    try:
        tag_name, argument = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.contents
        raise template.TemplateSyntaxError(msg)
    return TestNode(argument)

@register.tag(name = 'up')
def comment_test(parser, token):
    nodelist = parser.parse(('down',))
    parser.delete_first_token()
    return UpNode(token.contents)

@register.tag(name = 'comment')
def comment_test(parser, token):
    nodelist = parser.parse(('endcomment',))
    parser.delete_first_token()
    return CommentNode()

class TestNode(template.Node):
    
    def __init__(self, argument):
        self.argument = argument[1:-1]

    def render(self, context):
        return self.argument

class CommentNode(template.Node):
    def render(self, context):
        return ''

class UpNode(template.Node):
    def __init__(self, argument):
        self.argument = argument

    def render(self, context):
        return self.argument
