$replacements = @(
    @{
        File = "blog\index.html"
        Old = "Abhee Projects — authorised channel partner for Abhee Pvt. Ltd. Explore Abhee New Dimension, Abhee Aaria, Abhee Celestial City, Abhee Silicon Shine and more luxury apartments across Bangalore. RERA approved. Zero brokerage."
        New = "Abhee Projects — authorised channel partner for Abhee. Explore premium RERA-approved luxury apartments across Bangalore. Zero brokerage."
    },
    @{
        File = "blog\varthur-sarjapur-road-real-estate-2026.html"
        Old = "Abhee Projects — authorised channel partner for Abhee Pvt. Ltd. Explore Abhee New Dimension, Abhee Aaria, Abhee Celestial City, Abhee Silicon Shine and more luxury apartments across Bangalore. RERA approved. Zero brokerage."
        New = "Abhee Projects — authorised channel partner for Abhee. Explore premium RERA-approved luxury apartments across Bangalore. Zero brokerage."
    },
    @{
        File = "blog\abhee-new-dimension-review-2026.html"
        Old = "Abhee Projects — authorised channel partner for Abhee Pvt. Ltd. Explore Abhee New Dimension, Abhee Aaria, Abhee Celestial City, Abhee Silicon Shine and more luxury apartments across Bangalore. RERA approved. Zero brokerage."
        New = "Abhee Projects — authorised channel partner for Abhee. Explore premium RERA-approved luxury apartments across Bangalore. Zero brokerage."
    },
    @{
        File = "blog\pre-launch-apartment-buying-guide-bangalore-2026.html"
        Old = "Abhee Projects — authorised channel partner for Abhee Pvt. Ltd. Explore Abhee New Dimension, Abhee Aaria, Abhee Celestial City, Abhee Silicon Shine and more luxury apartments across Bangalore. RERA approved. Zero brokerage."
        New = "Abhee Projects — authorised channel partner for Abhee. Explore premium RERA-approved luxury apartments across Bangalore. Zero brokerage."
    },
    @{
        File = "blog\abhee-new-dimension-lifestyle-amenities.html"
        Old = "Discover the unmatched lifestyle at Abhee New Dimension on Varthur Sarjapur Road. Featuring 140+ amenities, a 3-acre golf driving range, and Scottish-themed luxury."
        New = "Discover the unmatched lifestyle at Abhee New Dimension on Varthur Sarjapur Road. Featuring 140+ amenities, 3-acre golf range, and Scottish-themed luxury."
    },
    @{
        File = "abhee-aaria.html"
        Old = "Abhee Aaria — premium 1, 2, 3 &amp; 4 BHK luxury apartments in Gunjur, off Sarjapur Road, Bangalore. Starting from ₹75.7 Lakhs*. RERA approved. Zero brokerage. Enquire for price and floor plans."
        New = "Abhee Aaria: Premium 1, 2, 3 &amp; 4 BHK luxury apartments in Gunjur, Bangalore. Starting from ₹75.7 Lakhs*. RERA approved, zero brokerage. Enquire today."
    },
    @{
        File = "abhee-celestial-city.html"
        Old = "Abhee Celestial City — premium 2 &amp; 3 BHK luxury apartments on Sarjapur Road, Bangalore. Starting from ₹1.30 Cr*. RERA approved. Zero brokerage. Enquire for price and floor plans."
        New = "Abhee Celestial City: Premium 2 &amp; 3 BHK luxury apartments on Sarjapur Road, Bangalore. From ₹1.30 Cr*. RERA approved, zero brokerage. Enquire for details."
    },
    @{
        File = "abhee-codename-new-dimension.html"
        Old = "Abhee Codename New Dimension – a 45-acre Scotland-themed luxury township on Varthur–Sarjapur Road, East Bangalore. 2 to 4.5 BHK apartments from ₹1.14 Cr*. 140+ amenities, 3-acre golf course, man-made lake. EOI open now."
        New = "Abhee Codename New Dimension: 45-acre Scotland-themed luxury township on Varthur-Sarjapur Road. 2 to 4.5 BHKs from ₹1.14 Cr*. 140+ amenities. EOI open now."
    },
    @{
        File = "abhee-silicon-shine.html"
        Old = "Abhee Silicon Shine — premium 1, 2, 3 &amp; 4 BHK apartments at Bommasandra, Bangalore. Starting from ₹70 Lakhs*. RERA approved. Close to Electronic City and Bommasandra Industrial Area. Zero brokerage."
        New = "Abhee Silicon Shine: Premium 1, 2, 3 &amp; 4 BHK apartments in Bommasandra, near Electronic City. From ₹70 Lakhs*. RERA approved, zero brokerage. Enquire now."
    },
    @{
        File = "blogs\scotland-themed-townships-bangalore-luxury-market\index.html"
        Old = "Explore why Scotland-themed townships are winning Bangalore's luxury real estate market. How Abhee Codename New Dimension on Varthur Sarjapur Road sets the benchmark."
        New = "Explore why Scotland-themed townships are winning Bangalore's luxury real estate market. Abhee Codename New Dimension on Varthur Sarjapur Road sets the benchmark."
    }
)

foreach ($item in $replacements) {
    $path = "c:\Users\vansh\OneDrive\Desktop\Abhee\Abhee v2\" + $item.File
    if (Test-Path $path) {
        $content = Get-Content $path -Raw
        $content = $content.Replace($item.Old, $item.New)
        Set-Content -Path $path -Value $content -NoNewline
    }
}
