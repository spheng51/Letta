# Letta-Rise360 Floating Assistant

This repository contains an example snippet for embedding a **Letta** AI chatbot in Articulate **Rise360** courses.

The goal is to provide instructional designers with a lightweight way to add an on-demand virtual tutor to their courses. The assistant appears as a floating chat bubble that learners can open whenever they need help.

## Usage

1. Export your course from Rise360 as a **Web** or **LMS** package and download the ZIP archive.
2. Extract the archive to a local folder on your computer.
3. Open the course's `index.html` file in a text editor.
4. Copy the markup from [`embed.html`](embed.html) and paste it immediately **before** the closing `</body>` tag in `index.html` (or any common layout file used by your course).
5. Replace the `agentId` value in the snippet with the ID of your own Letta agent.
6. Save the file and re‑zip the course if required by your LMS.
7. Upload the updated package to your LMS or web host.

When learners view the course, the Letta bubble will appear in the corner of the screen. Clicking it opens a chat window connected to your configured Letta agent.

### Optional: automate the injection

You can use the helper script in the `scripts/` directory to insert the snippet automatically:

```bash
python scripts/inject_snippet.py path/to/index.html
```

Pass a second argument to specify a custom snippet file. After running the script, deploy the course as usual.

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

Include this snippet in your course files to enable the assistant.
