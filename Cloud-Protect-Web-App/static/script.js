document.addEventListener("DOMContentLoaded", function() {
    // Example: Handle form submission
    const newsletterForm = document.querySelector(".newsletter-signup form");
    newsletterForm.addEventListener("submit", function(e) {
        e.preventDefault();
        alert("Thank you for subscribing!");
    });

    // Handle links with the class 'cta-button' for redirection
    const links = document.querySelectorAll("a.cta-button, a.cta-button1");
    links.forEach(link => {
        link.addEventListener("click", function(e) {
            e.preventDefault();
            const href = this.getAttribute("href");
            showLoadingScreen();
            setTimeout(() => {
                window.location.href = href;
            }, 1000); // Adjust delay as needed
        });
    });

    // Function to show the loading screen
    function showLoadingScreen() {
        const loadingScreen = document.getElementById("loading-screen");
        loadingScreen.classList.add("show");
    }

    // Function to reveal elements on scroll
    function revealOnScroll() {
        var reveals = document.querySelectorAll('.reveal');

        for (var i = 0; i < reveals.length; i++) {
            var windowHeight = window.innerHeight;
            var elementTop = reveals[i].getBoundingClientRect().top;
            var elementVisible = 150;

            if (elementTop < windowHeight - elementVisible) {
                reveals[i].classList.add('active');
            } else {
                reveals[i].classList.remove('active');
            }
        }
    }

    // Add scroll event listener
    window.addEventListener('scroll', revealOnScroll);

    // To reveal elements that are already in view on page load
    revealOnScroll();
});
