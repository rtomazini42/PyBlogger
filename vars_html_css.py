
common_head_intro = """
<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" type="text/css" href="css/reset.css">
            <link rel="stylesheet" type="text/css" href="css/styles.css">
            <link rel="stylesheet" type="text/css" href="css/index.css">
            <title>""" 

common_head_middle = """ - Home</title>
        </head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <body>
            <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="posts.html">Posts</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="about.html">About</a></li>
            </ul>

"""

close_body = """
        </body>
        </html>
"""


def creation_index(name):
    content =         """
            <h1>Index</h1>
        """ 
    html_content = common_head_intro  + name + common_head_middle + content + close_body
    return html_content


def creation_posts(name):
    content =         """
            <h1>posts</h1>
        """ 
    html_content = common_head_intro  + name + common_head_middle + content + close_body
    return html_content

def creation_contact(name):
    content =         """
            <h1>Contacts</h1>
        """ 
    html_content = common_head_intro  + name + common_head_middle + content + close_body
    return html_content

def creation_about(name):
    content =         """
            <h1>About</h1>
        """ 
    html_content = common_head_intro  + name + common_head_middle + content + close_body
    return html_content


def creation_reset_css():
    css_content = """
        
        /* http://meyerweb.com/eric/tools/css/reset/ 
    v2.0 | 20110126
    License: none (public domain)
    */

    html, body, div, span, applet, object, iframe,
    h1, h2, h3, h4, h5, h6, p, blockquote, pre,
    a, abbr, acronym, address, big, cite, code,
    del, dfn, em, img, ins, kbd, q, s, samp,
    small, strike, strong, sub, sup, tt, var,
    b, u, i, center,
    dl, dt, dd, ol, ul, li,
    fieldset, form, label, legend,
    table, caption, tbody, tfoot, thead, tr, th, td,
    article, aside, canvas, details, embed, 
    figure, figcaption, footer, header, hgroup, 
    menu, nav, output, ruby, section, summary,
    time, mark, audio, video {
        margin: 0;
        padding: 0;
        border: 0;
        font-size: 100%;
        font: inherit;
        vertical-align: baseline;
    }
    /* HTML5 display-role reset for older browsers */
    article, aside, details, figcaption, figure, 
    footer, header, hgroup, menu, nav, section {
        display: block;
    }
    body {
        line-height: 1;
    }
    ol, ul {
        list-style: none;
    }
    blockquote, q {
        quotes: none;
    }
    blockquote:before, blockquote:after,
    q:before, q:after {
        content: '';
        content: none;
    }
    table {
        border-collapse: collapse;
        border-spacing: 0;
    }
    """
    return css_content

def creation_styles_css(style_opt):
    #implementar depois opções
    if style_opt == 1:
        color1 = "#333"
        color2 = "#111"
    else:
        color1= "#1d9bf0"
        color2 = "#111"
    css_content = """
                                        ul {
                        list-style-type: none;
                        margin: 0;
                        padding: 0;
                        overflow: hidden;
                        background-color: """+ color1 +  """;
                        }

                        li {
                        float: left;
                        }

                        li a {
                        display: block;
                        color: white;
                        text-align: center;
                        padding: 14px 16px;
                        text-decoration: none;
                        }

                        li a:hover {
                        background-color: """+ color2 +  """;
                        }
            """

    return css_content