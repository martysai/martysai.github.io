---
title: "Building a Personalized Autonomous Agent with OpenClaw, Azure, and GitHub Copilot"
permalink: /building-personalized-agent-openclaw-with-azure-and-github-copilot/
header:
  overlay_color: "#333"
author_profile: true
toc: true
classes: wide
related: false
share: false
---

I wanted a personal agent that was actually useful day to day — not a demo chatbot, not a thin wrapper around a single model, and not an expensive always-on research toy. The goal was a practical autonomous assistant that could live close to my tools, remember context, run scheduled workflows, inspect code, work with documents, and still stay cheap enough to operate as personal infrastructure.

This post is a write-up of how I built that system around [OpenClaw](https://github.com/openclaw/openclaw), a small Azure VM, GitHub Copilot-backed model access, Microsoft 365 integrations, and a few carefully routed specialist lanes.

> Draft note: expand this into the full story — architecture, costs, reliability lessons, and the routing model.

## What I wanted

The system had to satisfy a few constraints:

- **Personalized:** it should know my workflows, repos, notes, scheduled digests, and preferences.
- **Autonomous, but bounded:** it should be able to run jobs and inspect systems, but not send emails, modify cloud drives, or take destructive actions without explicit approval.
- **Cheap:** default reasoning should run through subscriptions I already pay for, especially GitHub Copilot.
- **Extensible:** specialized routes should exist for Microsoft 365 content, deep research, and financial analysis without becoming the default path.
- **Auditable:** scheduled tasks, provider choices, and external actions should be visible and explainable.

## Architecture at a glance

The current setup is roughly:

- **OpenClaw** as the agent runtime and orchestration layer.
- **Azure VM** as the always-on host.
- **GitHub Copilot-backed model** as the default reasoning path.
- **Sonnet 4.5** as a general fallback when the default provider is not enough or unavailable.
- **Microsoft 365 / Graph / Copilot API route** for OneDrive and M365-grounded document work.
- **Personal Claude subscription** as a scarce specialist lane for deep research and financial-analysis digests.
- **Cron-based workflows** for scheduled jobs.
- **Explicit approval gates** for email sending, calendar writes, and cloud-drive modifications.

## The key design decision: routing, not one giant model

A personal agent should not treat every task as the same kind of model call.

The routing model I ended up with is:

| Workflow | Provider route |
| --- | --- |
| Normal chat, coding, repo inspection | GitHub Copilot-backed model |
| General fallback | Sonnet 4.5 |
| M365 / OneDrive / SharePoint / Teams questions | Microsoft 365 Copilot API / Graph |
| Deep research digests | Personal Claude subscription |
| Financial analysis digest | Personal Claude subscription only; no fallback |

This keeps the system cheap and predictable. GitHub Copilot handles the everyday work. Microsoft stays the boundary for Microsoft 365 data. Claude is reserved for workflows where long-form synthesis is worth spending scarce quota.

## Safety rails that matter in practice

The boring parts are what make the system usable:

- Emails are never sent without per-message approval.
- Calendar writes require explicit confirmation.
- OneDrive and Google Drive are read-only by default, with hard no-delete/no-overwrite rules.
- Financial analysis is research support only — no trades, no broker actions, no pretending to be regulated advice.
- Scheduled workflows write local drafts/reports first, then ask for approval before external delivery.

## What worked well

TODO:

- GitHub Copilot as the everyday model lane.
- OpenClaw cron jobs for durable scheduled work.
- Local filesystem drafts for reviewable outputs.
- Specialist lanes instead of uncontrolled fallback chains.
- Treating memory and preferences as files rather than vibes.

## What was harder than expected

TODO:

- Provider quirks and encrypted/reasoning payload errors.
- Telegram/session timeout failure modes.
- Email delivery rendering.
- Local VM memory limits.
- Avoiding accidental data egress across provider boundaries.

## Cost model

TODO: add rough monthly cost breakdown:

- Azure VM.
- GitHub Copilot subscription.
- Claude personal subscription.
- Microsoft 365 Copilot subscription.
- Optional APIs / search tooling.

## Example workflow: financial analyst digest

TODO: describe the Wednesday morning workflow:

1. Read the workbook snapshot locally, read-only.
2. Gather public financial sources.
3. Send minimized source notes to Claude.
4. Produce a local report and email draft.
5. Ask for explicit approval before sending.

## Conclusion

TODO: final framing — the interesting part is not that an agent can call tools. It is that a personal agent can become reliable infrastructure when model routing, permissions, memory, and scheduled workflows are treated as first-class engineering problems.
