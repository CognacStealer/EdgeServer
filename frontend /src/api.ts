const API_BASE_URL = "http://127.0.0.1:8000";

export async function predict(input: string, userToken: string) {
  const response = await fetch(`${API_BASE_URL}/predict?input=${encodeURIComponent(input)}`, {
    headers: { "x-api-key": userToken }
  });

  if (!response.ok) {
    throw new Error(`Error ${response.status}: ${response.statusText}`);
  }

  return await response.json();
}
