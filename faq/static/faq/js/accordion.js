const accordionItems = document.querySelectorAll(".accordion-item");

/**
 * FAQ page accordion layout These Javascript is coming from 
 * SheCodes - [JavaScript] - How to create an Accordion with JavaScript
 * https://www.shecodes.io/athena/9202-how-to-create-an-accordion-with-javascript
 */
accordionItems.forEach(item =>
  item.addEventListener("click", () => {
    const isItemOpen = item.classList.contains("open");
    accordionItems.forEach(item => item.classList.remove("open"));
    if (!isItemOpen) {
      item.classList.toggle("open");
    }
  })
);