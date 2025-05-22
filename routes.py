import logging
from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from models import Lead

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-lead', methods=['POST'])
def submit_lead():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        accept_communications = 'accept_communications' in request.form
        
        # Validate required fields
        if not name or not email or not phone:
            flash('Por favor, preencha todos os campos obrigatórios.', 'error')
            return redirect(url_for('index'))
        
        # Create new lead
        new_lead = Lead()
        new_lead.name = name
        new_lead.email = email
        new_lead.phone = phone
        new_lead.accept_communications = accept_communications
        
        db.session.add(new_lead)
        db.session.commit()
        
        # Store name in session for personalized success message
        session['name'] = name
        
        flash('Dados enviados com sucesso!', 'success')
        return redirect(url_for('success'))
    
    except Exception as e:
        logging.error(f"Error submitting lead: {str(e)}")
        flash('Ocorreu um erro ao processar sua solicitação. Por favor, tente novamente.', 'error')
        return redirect(url_for('index'))

@app.route('/success')
def success():
    name = session.get('name', '')
    return render_template('success.html', name=name)

@app.route('/termos')
def terms():
    return render_template('terms.html')

@app.route('/privacidade')
def privacy():
    return render_template('privacy.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404

@app.errorhandler(500)
def server_error(e):
    logging.error(f"Server error: {str(e)}")
    return render_template('index.html'), 500
