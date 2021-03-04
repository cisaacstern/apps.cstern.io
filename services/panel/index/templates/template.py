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

<p id="description">
    {{ description }}
    These are apps by <a href="https://cstern.io" class="txt">Charles Stern</a>.
    If a project isn't an app, it might be a 
    <a href="https://cstern.io/projects?tags=site" class="txt">#site</a>, 
    <a href="https://cstern.io/projects?tags=analysis" class="txt">#analysis</a>, or 
    <a href="https://cstern.io/projects?tags=feature" class="txt">#feature</a>.
</p>
<br>
<div class="container">
<ul>
    {% for app in apps %}

    <li>
    <h1>
        <i id="{{ app['name'] }}-btn" class="fas fa-caret-right">
            <span class="title"> {{ app['name'] }} <span>
        </i>
        <a href="https://apps.cstern.io/{{ app['name'] }}" target="_blank">
            <span class="change-icon">
            <i class="fas fa-external-link-square-alt"></i>
            <i class="fas fa-external-link-alt"></i>
            </span>
        </a>
    </h1>
    <blockquote id="{{ app['name'] }}-block" class="invisible">
        <a href="https://github.com/cisaacstern/{{ app['name'] }}" target="_blank">
            <img class="round-corners" alt="GitHub" 
                    src="{{ badge['base'] + app['name'] + badge['tail']}}">
        </a>
        <p>
            {{ app['description'] }}
        </p>
        <a href="https://cstern.io/projects/{{ app['name'] }}">
            <span class="change-icon read">
            <i class="fas fa-book-open"></i>
            <i class="fas fa-book-reader"></i>
            </span>
        </a>
    </blockquote></li>
    {% endfor %}
</div>

{% for app in apps %}
<script type='text/javascript'>

    var {{ app['js_var'] }}Block = document.getElementById("{{ app['name'] }}-block");
    var {{ app['js_var'] }}Btn = document.getElementById("{{ app['name'] }}-btn");

    function openClose(){
        if ({{ app['js_var'] }}Block.className == "invisible") {
            {{ app['js_var'] }}Block.className = "visible";
            {{ app['js_var'] }}Btn.className = "fas fa-caret-down";
        } else {
            {{ app['js_var'] }}Block.className = "invisible";
            {{ app['js_var'] }}Btn.className = "fas fa-caret-right";
        }
    }

    {{ app['js_var'] }}Btn.addEventListener('click', openClose);
</script>
{% endfor %}

{% endblock %}
"""
