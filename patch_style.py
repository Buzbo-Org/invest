import re

with open("style.css", "r") as f:
    content = f.read()

# Replace the old media query block with the new one
old_media = """/* Responsive */
@media (max-width: 768px) {
  .nav-links { display: none; } /* Simplify for mobile for now */
  .thesis-grid, .product-container, .model-grid, .invest-terms {
    grid-template-columns: 1fr;
  }
  .hero-title { font-size: 2.5rem; }
  .proof-stats { flex-direction: column; gap: 2rem; }
  .invest-box { padding: 2rem; }
}"""

new_media = """/* Responsive */
@media (max-width: 768px) {
  .nav-links { display: none; } /* Simplify for mobile for now */
  
  .thesis-grid, .product-container, .invest-terms {
    grid-template-columns: 1fr !important;
  }
  
  .hero-title { font-size: 2.5rem; white-space: normal !important; line-height: 1.1; }
  
  .swipe-on-mobile {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    scroll-snap-type: x mandatory !important;
    gap: 1.5rem !important;
    padding-bottom: 2rem !important;
    margin-bottom: 1rem !important;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none; /* Firefox */
  }
  
  .swipe-on-mobile::-webkit-scrollbar {
    display: none; /* Safari and Chrome */
  }

  .swipe-on-mobile > * {
    flex: 0 0 85% !important; /* Take up most of the screen but peek the next */
    scroll-snap-align: center !important;
  }
  
  /* Additional layout overrides to prevent long pages */
  #intro .container { padding: 0 1rem; }
  .section-title { font-size: 2rem; }
  
  #proof { padding: 8rem 0 3rem 0 !important; }
  #proof .section-header { margin-bottom: 5rem !important; }
  
  /* Ask section grid stacking */
  #invest .container > div[style*="display: grid"] {
      grid-template-columns: 1fr !important;
      gap: 2rem !important;
  }
  #invest .container > div[style*="display: grid"] > div:first-child {
      min-height: 250px !important;
      background-size: contain !important;
  }
  
  /* Fix problem grid stacking */
  .problem-wrapper {
      grid-template-columns: 1fr !important;
  }
  
  /* Fix text alignments to be more mobile friendly */
  h2, h3 { line-height: 1.2 !important; }
  
  .footer-links { flex-direction: column; align-items: center; gap: 1.5rem; }
}"""

if old_media in content:
    content = content.replace(old_media, new_media)
else:
    print("Warning: old_media not found, appending instead.")
    content += "\n" + new_media

with open("style.css", "w") as f:
    f.write(content)

