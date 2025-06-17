export default {
  async fetch(request) {
    if (request.method !== "POST") {
      return new Response("Method Not Allowed", { status: 405 });
    }

    try {
      const payload = await request.json();
      const eventType = request.headers.get("X-GitHub-Event");
      const repo = payload.repository?.full_name;

      console.log(`Received ${eventType} from ${repo}`);

      return new Response("Webhook received", { status: 200 });
    } catch (err) {
      return new Response("Invalid JSON", { status: 400 });
    }
  }
}
