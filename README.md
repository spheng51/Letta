# Letta-Rise360 Floating Assistant

This repository contains an example snippet for embedding a **Letta** AI chatbot in Articulate **Rise360** courses.

The goal is to provide instructional designers with a lightweight way to add an on-demand virtual tutor to their courses. The assistant appears as a floating chat bubble that learners can open whenever they need help.

## Usage

1. Publish your Rise360 course (web or LMS package).
2. Insert the code from [`embed.html`](embed.html) into the course's `index.html` (or a common layout file) just before the closing `</body>` tag.
3. Replace the `agentId` placeholder (`your-agent-id`) with the ID from your Letta account.
4. Upload the modified course to your LMS or web host.

When learners view the course, the Letta bubble will appear in the corner of the screen. Clicking it opens a chat window connected to your configured Letta agent.

## Project Plan

The long-term project aims to develop a full toolkit for configuring and injecting this chat widget automatically. Planned milestones include:

- **MVP:** simple embed script and manual configuration.
- **Beta:** user-friendly configuration UI and persistent sessions.
- **v1.0:** polished UI, analytics options, and comprehensive documentation.

See the project plan in the repository discussions for more details.

## Example Snippet

```html
<script>
  window.lettaSettings = {
    agentId: "your-agent-id",
    bubblePosition: "bottom-right",
    bubbleColor: "#0055A4",
    greetingText: "Need help? Ask me anything!",
    theme: {
      fontFamily: "Arial, sans-serif",
      fontSize: "16px"
    }
  };
</script>
<script src="https://cdn.getletta.com/let.js" async></script>
```

Include this snippet in your course files to enable the assistant. Make sure to
replace `your-agent-id` with the ID assigned to your bot in the Letta dashboard.
