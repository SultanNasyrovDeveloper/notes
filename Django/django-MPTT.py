###############
# DJANGO_MPTT #
###############
# efficient way to store hierarchical data in flat structure


# When to use
# много классов описывают один и тот же базовый тип контента:
Головной офис --> Региональный офис --> Корпорации - все относится к типу офис

# INSTALLATION
# -------------
# install with pip
pip install django-mptt
# add to INSTALLED APPS
'mptt'

# basic MPTTModel
# ----------------
from mptt.models import MPTTModel, TreeForeignKey


class SomeModel(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')

    class MPTTMeta:
        ordering = ('name', )


# MODEL INSTANCE METHODS
# ======================

# получить queryset содеражащий предков экземпляра
get_ancestors(ascending=True, insclude_self=False)
# получить queryset содеражащий непосредственных потомков экземпляра
# то есть узлы на один уровень ниже чем текущий
get_children()
# возвращает queryset содеражащий дочерние элементы в древовидном порядке
get_descendants(include_self=False)
# возвращает количество потомков, без запроса к БД
get_descendant_count()
# получить все дерево
get_family()
# следующего родственного экземпляра(одного уровня с ним)
get_next_sibling()
# предыдущий родственный экземпляр
get_previous_sibling()
# корневой узел
get_root()
# возвращает все родственные узлы
get_siblings(include_self=False)
# вставка элемента в дерево(для элементов, которых нет в дереве на данный момент)
insert_at()
    target  # узел относительно которого будет позиционироваться элементв
    position='first-child'
    save=False # будет вызван метод модели save()

is_child_node()  # True  if child
is_leaf_node()  # True if leaf
is_root_node()  # True if root
move_to(target, position='first-child')


# TREE MANAGER
# =============


# TEMPLATE
# =========
{% load mptt_tags %}
<ul>
    {% recursetree genres %}
        <li>
            {{ node.name }}
            {% if not node.is_leaf_node %}
                <ul class="children">
                    {{ children }}
                </ul>
            {% endif %}
        </li>
    {% endrecursetree %}
</ul>
