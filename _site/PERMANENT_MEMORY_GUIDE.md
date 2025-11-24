# Guide to Permanent Memory for AI Agents

This guide explains how to use `.github/copilot-instructions.md` as a "permanent memory" for AI agents (like GitHub Copilot or other coding assistants) working on this repository.

## What is the Permanent Memory File?

The file located at `.github/copilot-instructions.md` serves as a persistent set of instructions and context for AI agents. Unlike the context window of a single chat session, which is temporary, this file provides a way to "teach" the agent about your project's specific conventions, architecture, and preferences once, and have it remembered for future interactions.

## Why Use It?

- **Consistency**: Ensures the agent always follows your specific coding style (e.g., "Always use `_bibliography/papers.bib`").
- **Context**: Provides architectural details that might not be obvious from looking at a single file (e.g., "This is a Jekyll site using the al-folio theme").
- **Efficiency**: Reduces the need to repeat the same instructions in every chat session.

## Best Practices

### 1. Keep it Up-to-Date
Treat this file like documentation. If you change a major architectural decision or add a new tool, update this file. If the instructions are outdated, the agent will give you outdated advice.

### 2. Be Specific
Vague instructions like "Write good code" are less helpful than specific ones like "Use `render_diffs` shorthand in artifacts" or "Always place PDFs in `assets/pdf/`".

### 3. Structure for Readability
Use Markdown headers to organize the file. This helps both you (the human) and the agent parse the information.
- **Project Overview**: High-level summary.
- **Architecture**: Key components and how they interact.
- **Conventions**: Naming rules, file locations, specific patterns.
- **Workflow**: How to build, test, and deploy.

## When to Update

- **New Features**: When you add a new major feature or integration (e.g., a new Jekyll plugin).
- **Refactoring**: If you change the directory structure or key file locations.
- **Correction**: If the agent repeatedly makes the same mistake, add a rule here to correct it (e.g., "Never use `var`, always use `const` or `let`").

## Current File Structure

The current `.github/copilot-instructions.md` is organized as follows:

- **Project Overview**: Identifies the site as a Jekyll/al-folio academic website.
- **Architecture**: Explains the publication system, content collections, and plugins.
- **Development Workflow**: Docker vs. native Jekyll commands.
- **Key Conventions**: BibTeX format, Liquid templates, theme customization.
- **File Organization**: Where things live.
- **Common Pitfalls**: Troubleshooting tips.
- **When Modifying Code**: Specific rules for adding content.

## Example Usage

If you want to ensure the agent knows about a new "Research Notes" collection you added:

1. Open `.github/copilot-instructions.md`.
2. Find the **Content Collections** section.
3. Add a new entry:
   ```markdown
   4. **`_notes/`**: Research notes (private collection, not displayed on homepage)
   ```
4. Save the file.

Now, when you ask the agent "Where should I put my new research note?", it should correctly direct you to `_notes/`.
