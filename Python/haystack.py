# HAYSTACK

# example model
class Note(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title


# INSTALLATION
# ------------
# install package with pip
pip install django-haystack

# install solr
curl -LO https://archive.apache.org/dist/lucene/solr/x.Y.0/solr-X.Y.0.tgz
mkdir solr
tar -C solr -xf solr-X.Y.0.tgz --strip-components=1
cd solr
./bin/solr start                                    # start solr
./bin/solr create -c tester -n basic_config         # create core named 'tester'

# add to INSTALLED_APPS folder
'haystack',

# settings.py
# you can choose search engine if you want to(Whoosh, ElasticsearchSearch, Solr)
# SOLR 4.x
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}
# SOLR 6.x
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/tester',                 # Assuming you created a core named 'tester' as described in installing search engines.
        'ADMIN_URL': 'http://127.0.0.1:8983/solr/admin/cores'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}

# HANDLING DATA
# -------------
# create search indexes

# search indexes are the way Haystack determine
# you create search index for each Model
# every field inside search index class will be input field in auto generated model
import datetime
from haystack import indexes
from myapp.models import Note


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    # requires only one field with document=True
    # should be the same name for all search indexes (text is convention)
    text = indexes.CharField(document=True, use_template=True)  # main field
    author = indexes.CharField(model_attr='user')  # can work with foreign key
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        """ Must return model instance """
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter()


# make search template
# templates/search/indexes/app_name/model_name_text.txt
{{ object.title }}
{{ object.user.get_full_name }}
{{ object.body }}


# add search view to your templates
path('search/', include('haystack.urls'))


# basic search template
{% extends 'base.html' %}

{% block content %}
    <h2>Search</h2>
    <form method="get" action=".">
        <table>
            {{ form.as_table }}
            <tr>
                <td>&nbsp;</td>
                <td><input type="submit" value="Search"></td>
            </tr>
        </table>
        {% if query %}
            <h3>Results</h3>

            {% for result in page.object_list %}
                <p>
                    <a href="{{ result.object.get_absolute_url }}">{{ result.object.title }}</a>
                </p>
            {% empty %}
                <p>No results found.</p>
            {% endfor %}

            {% if page.has_previous or page.has_next %}
                <div>
                    {% if page.has_previous %}<a href="?q={{ query }}&amp;page={{ page.previous_page_number }}">{% endif %}&laquo; Previous{% if page.has_previous %}</a>{% endif %}
                    |
                    {% if page.has_next %}<a href="?q={{ query }}&amp;page={{ page.next_page_number }}">{% endif %}Next &raquo;{% if page.has_next %}</a>{% endif %}
                </div>
            {% endif %}
        {% else %}
        {% endif %}
    </form>
{% endblock %}


# reindex
# create search index (if exists will be deleted and created again)
python manage.py rebuild_index

# update existing search index
python manage.py update index
