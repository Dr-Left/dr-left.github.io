---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
redirect_from:
- /projects.html
---

<style>
    .project-title {
        font-size: 1.2em;
        margin-bottom: 1em;

    }

    .project-title:hover {
        color: blue;
    }

    .project-image {
        height: 120px;
        margin-right: 20px;
        flex-shrink: 0;
    }

    .project-image:hover {
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .project-text {
        font-size: 1em;
    }

    .project-labels {
        font-size: 14px;
        margin-top: 6px;
        margin-bottom: 0;
        color: gray;
    }

    .project-entry {
        padding: 10px 14px;
        border-radius: 6px;
        transition: background-color 0.2s ease-in-out;
    }

    .project-entry:hover {
        background-color: #f3f7fd;
    }

    @media (max-width: 600px) {
        .project-entry {
            flex-direction: column;
        }
        .project-image {
            height: auto;
            width: 80px;
            margin-right: 0;
            margin-bottom: 12px;
        }
    }
</style>

<div class="project-entry" style="margin: 1em 0; display: flex; align-items: flex-start;">

    <img src="/images/slack_ai_bot.png"
        class="project-image" alt="Slack Paper Bot">

    <div>
        <a class="project-title" href="https://github.com/Dr-Left/Slack-Paper-Bot">Slack Paper Bot</a><br>
        <text class="project-text"><b>Slack Paper Bot</b> is a personalized arXiv paper recommendation bot for Slack. It fetches recent papers, scores them against each user's interest profile using SPECTER2 semantic embeddings, and posts a daily digest to configured channels. Users can react with 🔥 to refine future recommendations, with optional GPT-4o-powered summaries.</text>
        <div class="project-labels">
            Written with Python
        </div>
        <div style="font-size: 14px; margin-top: 10px;">
            <a href="https://github.com/Dr-Left/Slack-Paper-Bot" style="text-decoration: none; color: blue;">[GitHub]</a>
        </div>
    </div>

</div>

<div class="project-entry" style="margin: 1em 0; display: flex; align-items: flex-start;">

    <img src="https://picx.zhimg.com/80/v2-7fafb4daebe2a9231e805f6b7d4c3561_1440w.webp?source=d16d100b"
        class="project-image" alt="Wordinary">

    <div>
        <a class="project-title" href="https://github.com/Dr-Left/Wordinary-v2">Wordinary v2.2.2</a><br>
        <text class="project-text"><b>Wordinary</b> is a powerful tool designed to streamline vocabulary building for English learners and educators. This software automates tasks such as extracting high-frequency words from texts, generating quizzes for vocabulary practice, and producing standard pronunciation audios.</text>
        <div class="project-labels">
            Year: 2021-2022, Written with Python and .NET
        </div>

        <div style="font-size: 14px; margin-top: 10px;">
            <a href="https://github.com/Dr-Left/wordinary/tree/master"><img src="../images/python.png"
                    alt="Python Backend" style="height: 30px; margin-right: 10px;"></a>
            <a href="https://github.com/Dr-Left/Wordinary-v2" style="text-decoration: none; color: blue;">[.NET
                Front End and Release]</a>
        </div>

    </div>



</div>