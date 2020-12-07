import xadmin
from xadmin import views
"""
list_display 控制列表展示的字段
search_fields 控制可以通过搜索框搜索的字段名称，xadmin使用的是模糊查询
list_filter 可以进行过滤操作的列
ordering 默认排序的字段
readonly_fields 在编辑页面的只读字段
exclude 在编辑页面隐藏的字段
list_editable 在列表页可以快速直接编辑的字段
show_detail_fileds 在列表页提供快速显示详情信息
refresh_times 指定列表页的定时刷新
list_export 控制列表页导出数据的可选格式
show_bookmarks 控制是否显示书签功能
data_charts 控制显示图标的样式
model_icon 控制菜单的图标
"""


class GlobalSettings(object):
    site_title = "安良成绩后台管理系统"
    site_footer = "安良在线成绩管理系统"
    # menu_style = "accordion"


class BaseSettings(object):
    # 开启换皮肤的功能
    enable_themes = True
    use_bootswatch = False
    """
       #xadmin默认是取消掉的，显示更多主题，可以打开为True，然后会请求https://bootswatch.com/api/3.json，
       如果请求失败，就只会显示两个默认的#请求的代码为 xadmin 下的plugins下的themes.py文件中 
       if self.use_bootswatch:（大概69行），会请求https://bootswatch.com/api/3.json加载，加载失败会只显示两个主题
    """
    user_themes = [
        {
            "name": "Cerulean",
            "description": "A calm blue sky",
            "thumbnail": "https://bootswatch.com/3/cerulean/thumbnail.png",
            "preview": "https://bootswatch.com/3/cerulean/",
            "css": "https://bootswatch.com/3/cerulean/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/cerulean/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/cerulean/bootstrap.min.css",
            "less": "https://bootswatch.com/3/cerulean/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/cerulean/variables.less",
            "scss": "https://bootswatch.com/3/cerulean/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/cerulean/_variables.scss"
        },
        {
            "name": "Cosmo",
            "description": "An ode to Metro",
            "thumbnail": "https://bootswatch.com/3/cosmo/thumbnail.png",
            "preview": "https://bootswatch.com/3/cosmo/",
            "css": "https://bootswatch.com/3/cosmo/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/cosmo/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/cosmo/bootstrap.min.css",
            "less": "https://bootswatch.com/3/cosmo/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/cosmo/variables.less",
            "scss": "https://bootswatch.com/3/cosmo/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/cosmo/_variables.scss"
        },
        {
            "name": "Cyborg",
            "description": "Jet black and electric blue",
            "thumbnail": "https://bootswatch.com/3/cyborg/thumbnail.png",
            "preview": "https://bootswatch.com/3/cyborg/",
            "css": "https://bootswatch.com/3/cyborg/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/cyborg/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/cyborg/bootstrap.min.css",
            "less": "https://bootswatch.com/3/cyborg/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/cyborg/variables.less",
            "scss": "https://bootswatch.com/3/cyborg/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/cyborg/_variables.scss"
        },
        {
            "name": "Darkly",
            "description": "Flatly in night mode",
            "thumbnail": "https://bootswatch.com/3/darkly/thumbnail.png",
            "preview": "https://bootswatch.com/3/darkly/",
            "css": "https://bootswatch.com/3/darkly/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/darkly/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/darkly/bootstrap.min.css",
            "less": "https://bootswatch.com/3/darkly/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/darkly/variables.less",
            "scss": "https://bootswatch.com/3/darkly/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/darkly/_variables.scss"
        },
        {
            "name": "Flatly",
            "description": "Flat and modern",
            "thumbnail": "https://bootswatch.com/3/flatly/thumbnail.png",
            "preview": "https://bootswatch.com/3/flatly/",
            "css": "https://bootswatch.com/3/flatly/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/flatly/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/flatly/bootstrap.min.css",
            "less": "https://bootswatch.com/3/flatly/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/flatly/variables.less",
            "scss": "https://bootswatch.com/3/flatly/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/flatly/_variables.scss"
        },
        {
            "name": "Journal",
            "description": "Crisp like a new sheet of paper",
            "thumbnail": "https://bootswatch.com/3/journal/thumbnail.png",
            "preview": "https://bootswatch.com/3/journal/",
            "css": "https://bootswatch.com/3/journal/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/journal/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/journal/bootstrap.min.css",
            "less": "https://bootswatch.com/3/journal/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/journal/variables.less",
            "scss": "https://bootswatch.com/3/journal/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/journal/_variables.scss"
        },
        {
            "name": "Lumen",
            "description": "Light and shadow",
            "thumbnail": "https://bootswatch.com/3/lumen/thumbnail.png",
            "preview": "https://bootswatch.com/3/lumen/",
            "css": "https://bootswatch.com/3/lumen/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/lumen/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/lumen/bootstrap.min.css",
            "less": "https://bootswatch.com/3/lumen/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/lumen/variables.less",
            "scss": "https://bootswatch.com/3/lumen/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/lumen/_variables.scss"
        },
        {
            "name": "Paper",
            "description": "Material is the metaphor",
            "thumbnail": "https://bootswatch.com/3/paper/thumbnail.png",
            "preview": "https://bootswatch.com/3/paper/",
            "css": "https://bootswatch.com/3/paper/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/paper/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/paper/bootstrap.min.css",
            "less": "https://bootswatch.com/3/paper/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/paper/variables.less",
            "scss": "https://bootswatch.com/3/paper/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/paper/_variables.scss"
        },
        {
            "name": "Readable",
            "description": "Optimized for legibility",
            "thumbnail": "https://bootswatch.com/3/readable/thumbnail.png",
            "preview": "https://bootswatch.com/3/readable/",
            "css": "https://bootswatch.com/3/readable/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/readable/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/readable/bootstrap.min.css",
            "less": "https://bootswatch.com/3/readable/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/readable/variables.less",
            "scss": "https://bootswatch.com/3/readable/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/readable/_variables.scss"
        },
        {
            "name": "Sandstone",
            "description": "A touch of warmth",
            "thumbnail": "https://bootswatch.com/3/sandstone/thumbnail.png",
            "preview": "https://bootswatch.com/3/sandstone/",
            "css": "https://bootswatch.com/3/sandstone/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/sandstone/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/sandstone/bootstrap.min.css",
            "less": "https://bootswatch.com/3/sandstone/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/sandstone/variables.less",
            "scss": "https://bootswatch.com/3/sandstone/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/sandstone/_variables.scss"
        },
        {
            "name": "Simplex",
            "description": "Mini and minimalist",
            "thumbnail": "https://bootswatch.com/3/simplex/thumbnail.png",
            "preview": "https://bootswatch.com/3/simplex/",
            "css": "https://bootswatch.com/3/simplex/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/simplex/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/simplex/bootstrap.min.css",
            "less": "https://bootswatch.com/3/simplex/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/simplex/variables.less",
            "scss": "https://bootswatch.com/3/simplex/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/simplex/_variables.scss"
        },
        {
            "name": "Slate",
            "description": "Shades of gunmetal gray",
            "thumbnail": "https://bootswatch.com/3/slate/thumbnail.png",
            "preview": "https://bootswatch.com/3/slate/",
            "css": "https://bootswatch.com/3/slate/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/slate/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/slate/bootstrap.min.css",
            "less": "https://bootswatch.com/3/slate/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/slate/variables.less",
            "scss": "https://bootswatch.com/3/slate/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/slate/_variables.scss"
        },
        {
            "name": "Spacelab",
            "description": "Silvery and sleek",
            "thumbnail": "https://bootswatch.com/3/spacelab/thumbnail.png",
            "preview": "https://bootswatch.com/3/spacelab/",
            "css": "https://bootswatch.com/3/spacelab/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/spacelab/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/spacelab/bootstrap.min.css",
            "less": "https://bootswatch.com/3/spacelab/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/spacelab/variables.less",
            "scss": "https://bootswatch.com/3/spacelab/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/spacelab/_variables.scss"
        },
        {
            "name": "Superhero",
            "description": "The brave and the blue",
            "thumbnail": "https://bootswatch.com/3/superhero/thumbnail.png",
            "preview": "https://bootswatch.com/3/superhero/",
            "css": "https://bootswatch.com/3/superhero/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/superhero/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/superhero/bootstrap.min.css",
            "less": "https://bootswatch.com/3/superhero/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/superhero/variables.less",
            "scss": "https://bootswatch.com/3/superhero/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/superhero/_variables.scss"
        },
        {
            "name": "United",
            "description": "Ubuntu orange and unique font",
            "thumbnail": "https://bootswatch.com/3/united/thumbnail.png",
            "preview": "https://bootswatch.com/3/united/",
            "css": "https://bootswatch.com/3/united/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/united/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/united/bootstrap.min.css",
            "less": "https://bootswatch.com/3/united/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/united/variables.less",
            "scss": "https://bootswatch.com/3/united/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/united/_variables.scss"
        },
        {
            "name": "Yeti",
            "description": "A friendly foundation",
            "thumbnail": "https://bootswatch.com/3/yeti/thumbnail.png",
            "preview": "https://bootswatch.com/3/yeti/",
            "css": "https://bootswatch.com/3/yeti/bootstrap.css",
            "cssMin": "https://bootswatch.com/3/yeti/bootstrap.min.css",
            "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/yeti/bootstrap.min.css",
            "less": "https://bootswatch.com/3/yeti/bootswatch.less",
            "lessVariables": "https://bootswatch.com/3/yeti/variables.less",
            "scss": "https://bootswatch.com/3/yeti/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/3/yeti/_variables.scss"
        }
    ]
    # 将use_bootswatch 设置为False ，不进行https://bootswatch.com/api/3.json请求加载，而是只使用user_themes，缺点就是不能动态加载，优点就是不会丢失


# 将写好的类注册到我们的xadmin类中
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)

