---
permalink: /
title: "Jingwei Zuo(左京伟)"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{{ site.data.profile.intro | markdownify }}

Email: {{ site.data.profile.email }}

Research 
-------

My main research question is:

👉  {{ site.data.profile.research_question }}
{: .notice}

<div class="disclosure">
  <div class="disclosure-summary">💡  How I develop such a research focus?</div>
  <div class="disclosure-panel">
    <div class="disclosure-panel-inner">
Nowadays, modern deep neural networks, represented by large language models (LLMs), have an enormous number of parameters and consume significant amounts of energy. Scaling up the model to achieve superior capabilities is important, whereas keeping the cost down is also important. The energy OpenAI’s ChatGPT uses each year to respond to the users’ requests could power 43,204 U.S. homes for the entire year.<a href="https://www.bestbrokers.com/forex-brokers/ais-power-demand-calculating-chatgpts-electricity-consumption-for-handling-over-78-billion-user-queries-every-year/#:~:text=That%20means%20the%20energy%20ChatGPT%20uses%20each%20year%20to%20handle%20requests%20could%20power%2043%2C204%20U.S.%20homes%20for%20an%20entire%20year">[1]</a> It is an outrageous number, which consolidates my belief that we should make every endeavor to cut down the cost of AI models, thereby making the new technology accessible to everybody and making the earth a greener one.
    </div>
  </div>
</div>


News
-------

{% include news-list.html %}


Publications
-------

{% include pub-list.html %}
<br>

Open Source Contributions
-------

{% include os-list.html %}
<br>

Experiences
-------

{% include exp-list.html %}
<br>

Educations
-------

{% include edu-list.html %}
<br>

Academic Services
-------

Service as a reviewer for the following conferences:
- NeurIPS 2025

To Learn More About Me
-------

<div class="disclosure">
  <div class="disclosure-summary">Ideals</div>
  <div class="disclosure-panel">
    <div class="disclosure-panel-inner">
I would love to witness a world where humans could obtain more convenience, harmony, and happiness. Undeniably, my current research interest is only one minute factor contributing to this grand (and probably quixote) ideal. But the thing is, I would not like my research to go against this prospect at any time and under any circumstance.

I advocate for the open source community.
    </div>
  </div>
</div>

<div class="disclosure">
  <div class="disclosure-summary">Other Experiences</div>
  <div class="disclosure-panel">
    <div class="disclosure-panel-inner">
I went to Northeastern University for a one-semester exchange program in 2023 Fall and had a gorgeous time there!

I love traveling around and have been to Hong Kong, Macao, Japan, Singapore, Australia, the US and of course many places of interest in mainland China.
    </div>
  </div>
</div>

<div class="disclosure">
  <div class="disclosure-summary">Fun Facts</div>
  <div class="disclosure-panel">
    <div class="disclosure-panel-inner">
When I get nervous, I like to scratch my hair😬. So next time you 
see me doing that in a debate, you know you've got me there.
    </div>
  </div>
</div>

<div class="disclosure">
  <div class="disclosure-summary">Hobbies</div>
  <div class="disclosure-panel">
    <div class="disclosure-panel-inner">
<ul>
{% for h in site.data.profile.hobbies %}<li><strong>{{ h.name }}:</strong> {{ h.detail }}</li>
{% endfor %}</ul>
    </div>
  </div>
</div>

Contacts
------

Feel free to reach out to me by email! We may even have an in-person coffee-chat if we are in the same city! I am always glad to talk to someone else, because other's talk often inspires me and my words may inspire others too:)

{% include globe.html %}

{% include gh-stars.html %}
{% include card-hover.html %}
