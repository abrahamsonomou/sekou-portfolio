
        messages.success(request,
        "Nous avons réçu votre message !",
        "alert alert-success alert-dismissible")
        connection = mail.get_connection()
        nom=form.cleaned_data['nom']
        email=form.cleaned_data['email']
        sujet=form.cleaned_data['sujet']
        message=form.cleaned_data['message']
        email1 = mail.EmailMessage(
        sujet,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        connection=connection,
        )
        
        email1.send() 
        
        connection.close()