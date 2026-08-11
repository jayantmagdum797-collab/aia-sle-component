# creating a ai agent
agent = Agent(name="MyAI", role="Assistant", goals=["Help users with tasks", "Provide information", "Learn from interactions"])     
my_agent = agent.create_agent() 
import { CopilotClient } from "@github/copilot-sdk";

const client = new CopilotClient();

await client.start();

const session = await client.createSession({
  model: "gpt-5.4",

  instructions: `
    You are a GitHub software engineering agent.

    Your job is to:
    1. Understand GitHub issues.
    2. Inspect repository code.
    3. Implement requested changes.
    4. Run relevant tests.
    5. Explain what you changed.
    6. Create a pull request when requested.
  `,

  availableTools: ["custom:*"],

  // GitHub authentication/token would be supplied here
});

const result = await session.sendAndWait({
  prompt: `
    Fix GitHub issue #142.

    Repository: my-company/my-app

    First inspect the issue and repository.
    Find the root cause.
    Implement the fix.
    Run the tests.
    Then prepare a pull request.
  `,
});

console.log(result?.data.content);

await client.stop();        

        