---
layout: default
---

{% for post in site.posts %}
## {{ post.date }} [{{ post.title }}]({{ post.url | relative_url }})

{% endfor %}
