from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname'].strip()
        lname = request.POST['lname'].strip()
        email = request.POST['email'].strip().lower()
        mobile = request.POST['mobile'].strip()
        password = request.POST['password']  # take password

        # 1. Checking if user already exists with same email
        if User.objects.filter(email=email).exists():
            msg = "You are already registered with this email. Please log in."
            return render(request, 'signup.html', {'msg': msg})

        # 2. Check mobile number length (should be exactly 10 digits)
        if not mobile.isdigit() or len(mobile) != 10:
            msg = "Mobile number must be exactly 10 digits."
            return render(request, 'signup.html', {'msg': msg})

        # 3. Strong password check
        if len(password) < 8:
            msg = "Password must be at least 8 characters long."
            return render(request, 'signup.html', {'msg': msg})

        # --- store signup data temporarily in session (NOT creating DB user yet) ---
        request.session['temp_user'] = {
            'fname': fname,
            'lname': lname,
            'email': email,
            'mobile': mobile,
            # store hashed password so created user is hashed
            'password': make_password(password),
        }

    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email'].strip().lower()
        password = request.POST['password']  # entered plain password

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            msg = "Email not matched. Please register first."
            return render(request, "login.html", {"msg": msg})
        
        print("Entered password:", password)
        print("DB password (hashed):", user.password)

        #Compare entered password with hashed one in DB
        if check_password(password, user.password):
            request.session['user_id'] = user.id  # store user in session
            return redirect('index')
        else:
            msg = "Invalid password. Please try again."
            return render(request, "login.html", {"msg": msg})

    return render(request, "login.html")


# Show all categories (Laptop, Camera, Accessories)
def categories_list(request):
    categories = Category.objects.all()
    return render(request, "categories_list.html", {"categories": categories})

# Show products inside a category (like all laptops: HP, Dell, etc.)
def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products.all()
    return render(request, "category_detail.html", {"category": category, "products": products})

def product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "product_detail.html", {"product": product})

# Show one product details
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "product_detail.html", {"product": product})

# Buy Now → Payment Page
def payment(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "payment.html", {"product": product})

# Payment Success Page
def payment_success(request):
    return render(request, "payment_success.html")
