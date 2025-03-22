function sendMail(){
    let parms={
        subject : document.getElementById("subject").value,
        message : document.getElementById("message").value,
    }

    emailjs.send("service_pb250zp","template_0vnt0bb",parms).then(alert("Email Sent"))
}