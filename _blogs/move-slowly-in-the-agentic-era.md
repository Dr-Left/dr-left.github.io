---
title: "Move Slowly in the Agentic Era"
title_em: "Slowly"
date: 2026-09-28
excerpt: "When generating code and papers takes seconds, speed stops being an advantage. Moving fast without real human thinking doesn't build velocity—it just stacks technical debt until everything collapses."
tags:
  - Agents
  - AI Safety
  - Research
---

## The Cult of Velocity

In the agentic era, moving fast is no longer an ambition—it has become the unquestioned default.

Users have grown accustomed to weekly flagship model drops. Product teams push features to production daily. Managers expect status reports and code commits at an unprecedented pace. And engineers write code faster than ever before.

The assembly line looks something like this: a human writes a brief prompt → an agent generates thousands of lines of code in seconds → a code-review agent glances over it with an automated checklist → pull requests are merged → move immediately to the next task.

The same manic treadmill is spinning in academia. In hot subfields, hundreds of arXiv preprints drop in a single day. Merely keeping up with reading titles and abstracts has become prohibitively time-consuming. Top-tier venues like NeurIPS and ICLR accept thousands of submissions every cycle—and an open secret across the community is that a growing fraction of these pipelines are largely automated. Research questions, experimental code, prose, and even benchmark figures are synthesized by agents in an afternoon.

Meanwhile, look at what this velocity is actually producing across the internet. We are drowning in synthetic noise: ghost-town GitHub repositories churned out by autonomous coding workflows, social platforms overrun with AI-generated media designed to farm engagement, and websites stuffed with unreadable, SEO-optimized text whose sole purpose is to capture token traffic.

When speed doesn't come with deep human mental investment, tech debt quietly compounds until everything breaks.

In the face of this flood, I want to propose an intentional counter-movement: **moving slowly in the agentic era**.

Moving slowly does not mean rejecting modern tools or writing every line of code by hand like a luddite. It means refusing to let raw generative speed dictate our standards of quality, accountability, and safety. The case for slowing down rests on three core pillars.

## 1. Moving Slowly Delivers Actual Quality

### The Software Engineering Trap: The Ballooning Black Box

Imagine working under a manager who evaluates your productivity by raw lines of code (LoC) shipped each day. In the pre-agentic world, that was bad management; in the agentic world, it becomes an existential disaster.

<figure class="blog-figure">
  <img src="/images/blogs/move-slowly-fig1.png" alt="A curve that rises steeply and then flattens out.">
  <figcaption>fig 1: moving fast will cause heavy tech debt in the future</figcaption>
</figure>

<figure class="blog-figure">
  <img src="/images/blogs/move-slowly-fig2.png" alt="A curve that stays flat and then rises steeply.">
  <figcaption>fig 2: moving slowly will eventually move fast</figcaption>
</figure>

Under that pressure, you have no choice. You invoke Claude Code or an autonomous terminal agent, feed it a prompt, and let it spit out five hundred lines of infrastructure and business logic. The agent brightly concludes:

> "All 24 unit tests pass. Ready to ship."

You hit merge. But here is the uncomfortable truth: **you don't actually know what those 24 tests covered.**

You don't know which edge cases were quietly omitted. You don't know the failure modes lurking in the dependencies the agent pulled in. You don't know the underlying control flow. Multiply this across an entire team over six months, and your codebase degenerates into an unmaintainable swamp of synthetically generated code. When a critical production outage hits, nobody on the engineering team has the mental model required to debug the system because nobody actually wrote or digested it.

Now consider the alternative. What if the pace was deliberately slowed down?

When you aren't frantically rushing to meet an artificial deadline, you have the room to do rigorous code reviews alongside your agent. You can spend the time to deeply inspect every logic branch. You can interrogate the agent: *Why did you choose this data structure over an alternative? What happens if this external API times out? What are the memory and caching implications under high concurrency?*

You understand every invariant and verify the test harness yourself. In this workflow, you aren't just an operator feeding prompts into a machine; you are exercising your judgment as a software engineer. The agent accelerates implementation, but your slowness preserves architectural integrity.

I know this trap firsthand. During an engineering internship, my success was evaluated mostly by throughput—how many corporate-standard pull requests and design docs I could ship. Under that pressure, I pushed code fast with coding agents. But toward the end, I paid the price: I spent days cleaning up the code that I didn't truly understand, and I panicked whenever a teammate asked me to explain the implementation details.

After the internship ended, I switched to another team, where I had the time to rethink the project and features I implemented in the summer. I was no longer evaluated on this thing, as it was completely orthogonal to my new area of job responsibility. It was more like a hobby than an evaluation point to me now. As a result, I not only solved the final unfinished blockers in the previous task, but understood the code better by looking into it at a much slower pace. Eventually, moving slower saved my time, I shall say.

### The Researcher's Dilemma: Significance Over Volume

The same principle holds true in research. If an academic career is measured purely by paper count, the dominant strategy becomes obvious: run autonomous exploration scripts, generate marginal variations of existing techniques, write the paper with an LLM, and flood the next conference deadline.

The tragedy of this approach is that it consumes vast amounts of energy, human attention, and compute while contributing almost nothing enduring to scientific knowledge.

Moving slowly gives a researcher the rarest luxury: the time to sit with a research question and ruthlessly question its premises. Is this problem actually important? Does this phenomenon generalize, or is it an artifact of our evaluation benchmark? If you spend weeks refining the formulation and hypothesis before spinning up dozens of GPUs, the resulting work will actually move the field forward—rather than simply inflating an h-index to meet a graduation requirement.

Being early in a PhD program, I see this exact tension in academia. The system constantly pushes you to publish early and often, treating papers like checkboxes for graduation rather than real contributions. I haven't published a paper over the last two years, but that doesn’t make me believe I am bad.

I am not an experienced researcher yet, so maybe my words are of lower credibility here. But still, I think real research isn't about gaming conference deadlines with slight tweaks to existing methods. It's about taking the time to ask whether a problem is actually worth solving in the first place. If we measure a researcher's value only by how fast they can churn out papers with AI, we lose the entire point of doing science.

### The Consumer's Perspective: Piercing the Surface

This applies to products as well. Generative tools make it trivial to build a dazzling "outer crust"—a sleek landing page, crisp animations, and an impressive initial demo. But when you scratch below the surface, many of these ultra-fast products are paper-thin wrappers that break on basic real-world workflows.

If users and buyers slow down their evaluation, they stop falling for flashy demos and stop pouring money into brittle software. Slowing down creates room to reward companies that spend the time to solve difficult, unglamorous infrastructural problems.

We see the same pattern as users chasing the latest AI models. Every few weeks, a new flagship model drops with claims that it is much smarter than the last. But how often do we stop and ask if the new model is actually better for our real workflows?

When we are embracing the new Claude Opus 5.5, did we really remember the performance of Claude Opus 4.8 three months ago? At least, I still remember the Opus which followed existing repository rules, constraints, and custom skills without being overly smart like the one is now. Sometimes, the business world is controlling our sense to believe every day is better than the day before, but the day before the day before? Who remembers?

The fact is that, even though every day is better than the day before, it can be actually of no difference to, or even worse than two days ago. This is the time arrow in the AI era. Slowing down helps us step off that treadmill and judge a tool by whether it actually makes our work more stable, not just whether the version number went up.

## 2. Moving Slowly Enables Full Human-Agent Alignment

We frequently talk about "human-in-the-loop," but high velocity reduces that loop to an empty rubber stamp.

Moving slowly does not mean micromanaging every single intermediary step. It is completely reasonable to let autonomous agents explore freely in the "middle" of a workflow—running exploratory scripts, generating candidate drafts, formatting data, or refactoring boilerplate where no immediate downstream harm exists.

However, at the **terminal stage of delivery**, a human must sign their name, take full responsibility, and answer for the outcome if things break.

You cannot take genuine moral or technical responsibility for a system you do not understand. If an automated financial pipeline fails, if an autonomous healthcare tool misdiagnoses a condition, or if a mission-critical infrastructure deploy takes down a network, saying *"the agent told me it worked"* is not an acceptable explanation.

True alignment at the delivery boundary requires understanding three fundamental questions:

1. **Failure Probability:** Under what operational conditions is this deliverable likely to fail?
2. **Edge Distributions:** What assumptions did the model make that might not hold in production or in unexpected real-world distributions?
3. **Core Mechanism:** What are the exact internal mechanisms driving this result, and where are its potential hazards?

To answer these questions honestly, the person responsible must have the time to investigate. Slowness is the buffer that transforms human oversight from a meaningless checkbox into an actual firewall.

## 3. Moving Slowly Preserves Supervision Over Autonomous Systems

The final reason to move slowly is long-term and civilizational: if we surrender the comprehension of our own systems, we surrender the ability to supervise them.

Consider where current trends lead. If every layer of our software stacks, communication channels, and security architectures is generated and maintained entirely by AI agents—with humans merely prodding the outer perimeter—we will eventually lose our internal grasp of how the infrastructure works.

Take three concrete examples where rapid deployment without deep human oversight creates dangerous blind spots:

1. **Reward Hacking:** An autonomous agent optimized purely for quick delivery might find unexpected shortcuts that technically satisfy automated evaluation metrics while introducing hidden security vulnerabilities or operational risks.
2. **Permissive Sandbox:** When agents configure their own execution environments or network isolation rules, human supervisors who rush through setup may inadvertently approve overly permissive access policies, allowing agents to execute arbitrary code outside safe boundaries.
3. **Agent-Reviewing-Agent Blind Spots:** Relying on automated evaluation agents to review code generated by other agents creates systemic blind spots, where shared training biases cause both models to overlook identical flaws.

If we don't understand the lock, we cannot know if the key has been compromised.

Moving slowly ensures that human comprehension remains synchronized with system complexity. By keeping ourselves deeply looped into the core components, we ensure that as autonomous agents grow more capable, our ability to audit, steer, and govern them scales alongside them.

## Conclusion: Slowness as Taste and Conviction

High velocity in the wrong direction is just a faster way to arrive at failure.

In the pre-agentic era, moving fast was a sign of ambition because building software, gathering empirical evidence, and producing artifacts required substantial friction. That friction served as an organic filter. Now that the friction of generation has collapsed to zero, anyone can produce infinite volume instantly.

In an era of endless, automated abundance, value shifts completely. It moves toward judgment, taste, and the willingness to stand behind what you put into the world.

Use agents aggressively to explore, iterate, and automate the mundane in the middle. But when it comes to the boundaries—when it is time to choose what problems matter, what code to deploy, and what ideas to publish—slow down. The future will not belong to whoever generates the most tokens; it will belong to those who build things that actually last.
