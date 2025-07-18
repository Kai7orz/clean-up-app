export default defineEventHandler(async (event) => {
  const res = await fetch("http://fast_api:8000/users/1/", {
    method: 'POST',
  });
  const blob = await res.blob();
  return new Response(blob, {
    headers: {
      'Content-Type': 'image/png',
    },
  });
});
