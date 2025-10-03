# Shonak Londhe - Portfolio Website

A modern, responsive portfolio website built with Django, featuring a machine learning demo for Indian real estate price prediction.

## 🌟 Features

- **Responsive Design**: Mobile-first approach with dark/light theme toggle
- **Project Showcase**: Display of featured projects with filtering
- **Blog System**: Technical blog posts with tags and categories
- **Contact Form**: Functional contact form with message storage
- **ML Demo**: Interactive Indian real estate price predictor
- **Admin Interface**: Django admin for easy content management

## 🛠️ Tech Stack

- **Backend**: Django 5.2.7, Python 3.x
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Database**: SQLite (development)
- **ML Libraries**: Scikit-learn, NumPy, Pandas
- **Styling**: Custom CSS with CSS Grid/Flexbox
- **Icons**: Font Awesome 6

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shonaklondhe/portfolio.git
   cd portfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Populate sample data**
   ```bash
   python manage.py populate_data
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit the application**
   - Portfolio: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 📱 Pages

- **Home**: Hero section with featured projects and recent blog posts
- **About**: Personal information and skills breakdown by category
- **Projects**: Portfolio showcasing ML projects (Crop Fertilizer Prediction, Weather Prediction, etc.)
- **Blog**: Technical articles and tutorials
- **ML Demo**: Interactive real estate price predictor for Indian market
- **Contact**: Contact form with email notifications and database storage
- **Resume**: Embedded Google Drive resume viewer with download option

## 🤖 ML Demo Features

The Indian Real Estate Price Predictor includes:
- **Multi-parameter input**: Bedrooms, Kitchen, Hall, Square Feet, City
- **City-based pricing**: Different multipliers for major Indian cities
- **Real-time prediction**: Instant price calculation with detailed breakdown
- **User-friendly interface**: Reset functionality and loading states

### Supported Cities
- Mumbai (Premium: 1.8x multiplier)
- Delhi (High: 1.6x multiplier)
- Bangalore (Mid-high: 1.4x multiplier)
- Pune (Mid: 1.2x multiplier)
- Hyderabad, Chennai (Standard: 1.1x multiplier)
- Kolkata (Budget: 0.9x multiplier)
- Ahmedabad (Affordable: 0.8x multiplier)
- Other cities (Base: 0.7x multiplier)

## 🎨 Design Features

- **Dark/Light Theme**: Toggle between themes with persistent storage
- **Responsive Layout**: Optimized for all device sizes
- **Smooth Animations**: CSS transitions and scroll animations
- **Modern UI**: Clean, professional design with good UX
- **Accessibility**: ARIA labels and keyboard navigation support

## 📊 Admin Interface

Access the Django admin at `/admin/` to manage:
- **Projects**: Add/edit portfolio projects
- **Blog Posts**: Create and publish articles
- **Skills**: Update skill proficiencies
- **Tags**: Organize content with colored tags
- **Contact Messages**: View and manage inquiries
- **ML Predictions**: Monitor prediction usage

## 🔧 Customization

### Email Configuration
For production email functionality:
1. Copy `.env.example` to `.env`
2. Set up Gmail app password (requires 2FA)
3. Update `EMAIL_HOST_PASSWORD` in `.env`
4. Uncomment SMTP settings in `settings.py`

### Adding New Projects
1. Login to admin interface
2. Go to Projects → Add Project
3. Fill in details, add tags, set as featured if desired

### Creating Blog Posts
1. Navigate to Blog Posts in admin
2. Create new post with content in Markdown
3. Set status to "Published" when ready

### Updating Skills
Current skill categories:
- **Frontend**: HTML/CSS, JavaScript
- **Backend**: Python, Django
- **Database**: SQL/Oracle (85%), SQLite3 (55%)
- **ML**: Scikit-learn, Machine Learning
- **Tools**: VSCode (90%), Git (85%)

## 📈 Performance

- **Optimized Images**: Lazy loading and proper sizing
- **Minified Assets**: Compressed CSS and JS
- **Database Queries**: Optimized with select_related and prefetch_related
- **Caching**: Template fragment caching for better performance

## 🔒 Security

- **CSRF Protection**: Django's built-in CSRF middleware
- **Input Validation**: Form validation and sanitization
- **SQL Injection Prevention**: Django ORM protection
- **XSS Protection**: Template auto-escaping

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Contact

- **Email**: shonaklondhe.it@gmail.com
- **LinkedIn**: [linkedin.com/in/shonaklondhe](https://www.linkedin.com/in/shonaklondhe/)
- **GitHub**: [github.com/shonaklondhe](https://github.com/shonaklondhe)

---

Built with ❤️ by Shonak Londhe
