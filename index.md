---
layout: default
---

{% for post in site.posts %}
## {{ post.date | date "%F" }} [{{ post.title }}]({{ post.url | relative_url }})

{% endfor %}
