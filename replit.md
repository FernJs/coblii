# COBLI Lead Generation System

## Overview

COBLI is a web application designed to capture leads from users interested in resolving PRF (Federal Highway Police) traffic fines with discounts or installment plans. The application provides a landing page with information about traffic fine services and a form to collect user contact information.

The system is built using Flask (Python) with a SQLAlchemy ORM layer for database management. It follows a simple MVC-like architecture with templates for the view layer, routes for controllers, and SQLAlchemy models for the data layer.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

The application follows a classic web application architecture:

1. **Frontend**: HTML, CSS, and JavaScript
   - Bootstrap 5 for responsive layout and components
   - Font Awesome for icons
   - AOS library for animations
   - Custom styling for branding and UI enhancements

2. **Backend**: Python Flask
   - Routes for handling HTTP requests
   - Templates for rendering HTML
   - SQLAlchemy for ORM and database operations

3. **Database**: SQLite (currently) but configurable to use PostgreSQL
   - Simple schema with a Lead model for storing user contact information

4. **Deployment**: Configured for Gunicorn with autoscaling

The system is designed to be simple yet scalable, with clean separation of concerns between data models, business logic, and presentation.

## Key Components

### Database Models (`models.py`)

The application uses a single model:

- **Lead**: Stores contact information collected from the landing page form
  - Fields include: name, email, phone, cpf (optional), accept_communications, created_at

The database is configured in `app.py` using SQLAlchemy, with support for both SQLite (development) and PostgreSQL (production) through environment variables.

### Routes (`routes.py`)

The application has three main routes:

1. `/` - Renders the landing page with the lead capture form
2. `/submit-lead` - Processes form submissions and stores lead data
3. `/success` - Displays success message after form submission

Additional page templates exist for privacy policy and terms of service, but routes for these pages haven't been implemented yet.

### Templates

The application uses Jinja2 templates organized in a hierarchy:

- `layout.html` - Base template with header, footer, and common elements
- Template pages that extend the base layout:
  - `index.html` - Landing page with lead capture form
  - `success.html` - Thank you page after form submission
  - `privacy.html` - Privacy policy
  - `terms.html` - Terms of use

### Static Assets

- CSS: Custom styling in `static/css/styles.css`
- JavaScript: Form handling and animations in `static/js/main.js`
- Images: Logo and possibly other assets in `static/img/`

## Data Flow

1. **Lead Capture**:
   - User visits the landing page
   - User fills out the contact form with name, email, phone, and optional CPF
   - Form is submitted to `/submit-lead` endpoint
   - Backend validates the input and stores the lead in the database
   - User is redirected to the success page

2. **Error Handling**:
   - If form validation fails, the user is redirected back to the form with error messages
   - Server errors are logged and a generic error message is displayed to the user

## External Dependencies

The application relies on several external libraries and services:

### Python Packages
- flask: Web framework
- flask-sqlalchemy: ORM for database access
- email-validator: For validating email addresses
- psycopg2-binary: PostgreSQL adapter (for production)
- gunicorn: WSGI HTTP server for production

### Frontend Libraries (CDN)
- Bootstrap 5: CSS framework
- Font Awesome: Icon library
- Google Fonts: Web fonts (Roboto and Montserrat)
- AOS: Animation library

## Deployment Strategy

The application is configured for deployment on Replit with:

1. **Gunicorn** as the WSGI server
   - Configured in `.replit` to run on port 5000
   - Uses `--reload` for development to automatically reload on code changes

2. **Database Options**
   - Development: SQLite (default)
   - Production: PostgreSQL (requires DATABASE_URL environment variable)

3. **Environment Variables**
   - DATABASE_URL: Connection string for the database
   - SESSION_SECRET: Secret key for session management

4. **Deployment Target**
   - Set to "autoscale" for optimal resource allocation

## Potential Improvements

1. **Authentication**: Add user authentication for an admin interface to view and manage leads
2. **API Endpoints**: Create REST API endpoints for integration with other systems
3. **Form Enhancements**: Add JavaScript validation for real-time feedback
4. **Analytics**: Add tracking for form submissions and page views
5. **Email Integration**: Send confirmation emails to leads after form submission
6. **Database Migration**: Implement a proper migration system for database schema changes
7. **Testing**: Add unit and integration tests
8. **Routes for Additional Pages**: Implement routes for privacy policy and terms of service pages