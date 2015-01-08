---
layout: default
img: voynich
img_link: "http://en.wikipedia.org/wiki/Voynich_manuscript"
caption: "The Voynich manuscript. As yet unread."
title: Bibliography
active_tab: bibliography
---

# Bibliography

## Papers

<ul>
{% for paper in site.data.bibliography.papers %}
    <li>
        {% if paper.url %}<a href="{{ paper.url }}">{{ paper.title }}</a>
        {% else %}{{ paper.title }}
        {% endif %}    
        ({{paper.author}}) paper.citation
    </li>
{% endfor %}
</ul>

## Books

<ul>
{% for book in site.data.bibliography.books %}
    <li>
        {% if book.url %}<a href="{{ book.url }}">{{ book.title }}</a>
        {% else %}{{ book.title }}
        {% endif %}    
        ({{book.author}})
    </li>
{% endfor %}
</ul>

