# Install and run your first local task

By the end of this tutorial you will have devops-skill installed for a project agent, and you will have initialized and finished one local-workflow tracing record.

## Prerequisites

- Node.js is not required for the skills themselves; Python 3 and git are.
- An AI agent that loads skills from `.agents/skills` (Codex) or an equivalent path.
- A git repository where you can create `tasks/`.

## Steps

1. Clone or open the [devops-skill](https://github.com/qdriven/devops-skill) repository.
2. From a target project root, install project-level skills (adjust path if you vendor the repo elsewhere):

   ```bash
   bash /path/to/devops-skill/dev-workflow-install.sh --project
   ```

3. Create a sample task file:

   ```bash
   mkdir -p tasks
   cat > tasks/hello.md <<'EOF'
   # Hello local workflow

   Write a one-line note that local-workflow tracing works.
   EOF
   ```

4. Initialize tracing:

   ```bash
   python3 .agents/skills/local-workflow/scripts/orchestrate.py init tasks/hello.md
   ```

5. Complete the tiny task (for example add `notes/hello.txt` with one line), then finish:

   ```bash
   python3 .agents/skills/local-workflow/scripts/orchestrate.py finish
   ```

6. Open `tasks/tracing/hello.md` and confirm status is completed.

You have completed a first local-workflow loop without creating a GitHub Issue.
