from fastapi import APIRouter
from fastapi.responses import JSONResponse
from email.message import EmailMessage

import ssl
import smtplib

mail_router = APIRouter()
mymail = 'utp0154571@alumno.utpuebla.edu.mx'
password = "bjvp pgvh gnfv qazj"


@mail_router.post('/mail', tags=['MAILS'], status_code=201)
def senMail(mailrec : str, name : str) :
    try:
        subject = "Mueblería Tico Confirmación"
        body = f"""
            Estimado cliente {name}
            Su solicitud ha sido revisada y aceptada.
            Mueblería TICO le hará llegar la información necesaria por este medio.

            Gracias por su preferencia.
        """
        em = EmailMessage()
        em['From'] = mymail
        em['To'] = mailrec
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
            smtp.login(mymail, password)
            smtp.sendmail(mymail, mailrec, em.as_string())


        return JSONResponse(status_code=201, content={'message' : f'message was sent succesfully'})

    except Exception as e:
        raise Exception(f'error : {e}')




