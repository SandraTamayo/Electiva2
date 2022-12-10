from flask import Flask,render_template,request
import boto3
app = Flask(__name__,static_url_path='',static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/solicitud", methods=["POST"])
def solicitar():
    Cant_lesiones_personales = request.form.get("Cant_lesiones_personales")
    Victconf_Amenaza = request.form.get("Victconf_Amenaza")
    Victconf_Desplazamiento_forzado = request.form.get("Victconf_Desplazamiento forzado")
    Cant_homicidios = request.form.get("Cant_homicidios")

    datos_a_enviar = "{},{},{}\n".format(float(Cant_lesiones_personales),float(Victconf_Amenaza),float(Victconf_Desplazamiento_forzado),float(Cant_homicidios))
    
    end_point = "sagemaker-scikit-learn-2022-12-06-15-14-41-444"
    

    client = boto3.client("sagemaker-runtime","us-east-1")


    response = client.invoke_endpoint(EndpointName=end_point,Body=2*datos_a_enviar,ContentType="text/csv")
    prediction = response['Body'].read()
    print(prediction)
    return f"{prediction}"



if __name__=="__main__":
    app.run(host="0.0.0.0", port=8000)



