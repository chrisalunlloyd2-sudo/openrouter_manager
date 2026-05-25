// Add event listeners to navigation links
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', event => {
        event.preventDefault();
        // Load corresponding page content
        const page = link.getAttribute('href');
        fetch(page)
            .then(response => response.text())
            .then(html => {
                document.querySelector('main').innerHTML = html;
            });
    });
});
```

[CMD]
```bash
mkdir project_cats_v2
cd project_cats_v2
touch README.md index.html styles.css script.js
