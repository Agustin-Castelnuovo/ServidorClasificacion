from fastapi import FastAPI, UploadFile, File
import requests
import base64

app = FastAPI()

# URL de tu PC local (Ngrok o Tailscale)
PC_URL = "https://barbless-jax-unerrant.ngrok-free.dev /clasificar_local"

@app.post("/clasificar")
async def clasificar(file: UploadFile = File(...)):
    # Leer imagen y convertir a base64
    image_bytes = await file.read()
    img_base64 = base64.b64encode(image_bytes).decode("utf-8")

    # Reenviar a tu PC
    try:
        resp = requests.post(PC_URL, json={"imagen": img_base64}, timeout=120)  # timeout largo
        print("Respuesta cruda del PC:", resp.text) 
        return resp.json()
    except Exception as e:
       print("❌ Error al enviar la imagen a la PC:", e)
       return {"error": str(e), "raw_response": resp.text if 'resp' in locals() else None}
