template = """
{% extends base %}

<!-- goes in body -->
{% block postamble %}
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/hack-font@3.3.0/build/web/hack-subset.css">
<link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Nunito">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css">
{% endblock %}

<!-- goes in body -->
{% block contents %}

<p id="description">{{ description }}</p>
<br>
<div class="container">
<ul>
    {% for app in apps %}

    <li>
    <h1>
        {{ app['name'] }}
        <a href="https://apps.cstern.io/{{ app['name'] }}" target="_blank">
            <span class="change-icon">
            <i class="fas fa-external-link-square-alt"></i>
            <i class="fas fa-external-link-alt"></i>
            </span>
        </a>
    </h1>
    <blockquote>
        <a href="https://github.com/cisaacstern/{{ app['name'] }}" target="_blank">
            <img class="round-corners" alt="GitHub" 
                    src="{{ badge['base'] + app['name'] + badge['tail']}}">
        </a>
        <p>
            {{ app['description'] }}
        </p>
        <a href="https://cstern.io/projects/{{ app['name'] }}" target="_blank">
            <span class="change-icon read">
            <i class="fas fa-book-open"></i>
            <i class="fas fa-book-reader"></i>
            </span>
        </a>
    </blockquote></li>
    {% endfor %}
</div>
{% endblock %}
"""
