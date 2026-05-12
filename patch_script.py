import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update LinkedIn URLs
content = content.replace(
    '''<a href="#" target="_blank" style="color: var(--cream); text-decoration: underline; font-size: 0.9rem;">LinkedIn &rarr;</a>
                </div>
                <div style="background: rgba(242,237,228,0.05); padding: 2rem; border-top: 2px solid var(--buzbo-red); display: flex; flex-direction: column;">
                    <h3 style="color: var(--cream); margin-bottom: 0.5rem; font-size: 1.5rem; text-transform: none;">Shinead Pond</h3>''',
    '''<a href="https://www.linkedin.com/in/elmerbulthuis/" target="_blank" style="color: var(--cream); text-decoration: underline; font-size: 0.9rem;">LinkedIn &rarr;</a>
                </div>
                <div style="background: rgba(242,237,228,0.05); padding: 2rem; border-top: 2px solid var(--buzbo-red); display: flex; flex-direction: column;">
                    <h3 style="color: var(--cream); margin-bottom: 0.5rem; font-size: 1.5rem; text-transform: none;">Shinead Pond</h3>'''
)

content = content.replace(
    '''Growth manager with lived experience of the problem, strong community-building instincts and hands-on experience in events, influencers and brand-led growth.</p>
                    <a href="#" target="_blank" style="color: var(--cream); text-decoration: underline; font-size: 0.9rem;">LinkedIn &rarr;</a>
                </div>
                <div style="background: rgba(242,237,228,0.05); padding: 2rem; border-top: 2px solid var(--charcoal); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">''',
    '''Growth manager with lived experience of the problem, strong community-building instincts and hands-on experience in events, influencers and brand-led growth.</p>
                    <a href="https://www.linkedin.com/in/shinead-pond-b4b589204/" target="_blank" style="color: var(--cream); text-decoration: underline; font-size: 0.9rem;">LinkedIn &rarr;</a>
                </div>
                <div style="background: rgba(242,237,228,0.05); padding: 2rem; border-top: 2px solid var(--charcoal); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">'''
)

# 2. Update Ask section to move the button to the full width
ask_old = """    <!-- 8. Invest -->
    <section id="invest" style="background-color: var(--charcoal); padding-top: 6rem; padding-bottom: 6rem;">
        <div class="container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 6rem; align-items: stretch;">
            <div style="background-image: url('3.png'); background-size: contain; background-position: center; border: 4px solid var(--dark-grey); filter: grayscale(10%); height: auto; min-height: 250px;"></div>
            
            <div>
                <span class="label" style="background-color: var(--cream); color: var(--buzbo-red); width: fit-content;">THE ASK</span>
                <h2 style="font-size: 5rem; color: var(--cream); font-family: var(--font-heading); line-height: 1; margin-top: 1rem; margin-bottom: 2rem;">JOIN THE VISION.</h2>
                <p style="font-size: 1.25rem; color: rgba(242,237,228,0.8); margin-bottom: 1.5rem;">We are scaling to 35M+ users, dominating the human-first hiring space, and working towards an IPO. The growth engine is proven.</p>
                <p style="font-size: 1.25rem; color: var(--amber); margin-bottom: 3rem; font-weight: bold;">Claim your stake in the next massive professional network.</p>
                
                <div style="display: flex; flex-direction: column; gap: 2rem; margin-bottom: 4rem;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1px solid rgba(242,237,228,0.1); padding-bottom: 1rem;">
                        <h5 style="text-transform: uppercase; font-size: 1rem; letter-spacing: 2px; color: rgba(240, 236, 228, 0.5); margin: 0;">Instrument</h5>
                        <p style="font-size: 2rem; font-family: var(--font-heading); font-weight: bold; color: var(--cream); margin: 0; line-height: 1;">SAFE (€1M)</p>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1px solid rgba(242,237,228,0.1); padding-bottom: 1rem;">
                        <h5 style="text-transform: uppercase; font-size: 1rem; letter-spacing: 2px; color: rgba(240, 236, 228, 0.5); margin: 0;">Valuation Cap</h5>
                        <p style="font-size: 2rem; font-family: var(--font-heading); font-weight: bold; color: var(--cream); margin: 0; line-height: 1;">€10M</p>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1px solid rgba(242,237,228,0.1); padding-bottom: 1rem;">
                        <h5 style="text-transform: uppercase; font-size: 1rem; letter-spacing: 2px; color: rgba(240, 236, 228, 0.5); margin: 0;">Allocation</h5>
                        <p style="font-size: 2rem; font-family: var(--font-heading); font-weight: bold; color: var(--cream); margin: 0; line-height: 1;">Max 2 Tickets</p>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1px solid rgba(242,237,228,0.1); padding-bottom: 1rem;">
                        <h5 style="text-transform: uppercase; font-size: 1rem; letter-spacing: 2px; color: rgba(240, 236, 228, 0.5); margin: 0;">Structure</h5>
                        <p style="font-size: 2rem; font-family: var(--font-heading); font-weight: bold; color: var(--cream); margin: 0; line-height: 1;">BV or INC</p>
                    </div>
                </div>
                
                <a href="mailto:hello@buzbo.com" class="btn btn-primary" style="font-size: 1.25rem; padding: 1.25rem 3rem; width: 100%; text-align: center; display: block; box-sizing: border-box; margin-top: 2rem;">CLAIM A TICKET &rarr;</a>
            </div>
        </div>
    </section>"""

ask_new = """    <!-- 8. Invest -->
    <section id="invest" style="background-color: var(--charcoal); padding-top: 6rem; padding-bottom: 6rem;">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 6rem; align-items: stretch;">
                <div style="background-image: url('5.png'); background-size: cover; background-position: center; border: 4px solid var(--dark-grey); filter: grayscale(10%); height: auto; min-height: 400px;"></div>
                
                <div>
                    <span class="label" style="background-color: var(--cream); color: var(--buzbo-red); width: fit-content;">THE ASK</span>
                    <h2 style="font-size: 5rem; color: var(--cream); font-family: var(--font-heading); line-height: 1; margin-top: 1rem; margin-bottom: 2rem;">JOIN THE VISION.</h2>
                    <p style="font-size: 1.25rem; color: rgba(242,237,228,0.8); margin-bottom: 1.5rem;">We are scaling to 35M+ users, dominating the human-first hiring space, and working towards an IPO. The growth engine is proven.</p>
                    <p style="font-size: 1.25rem; color: var(--amber); margin-bottom: 3rem; font-weight: bold;">Claim your stake in the next massive professional network.</p>
                    
                    <div style="display: flex; flex-direction: column; gap: 2rem; margin-bottom: 2rem;">
                        <div style="display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1px solid rgba(242,237,228,0.1); padding-bottom: 1rem;">
                            <h5 style="text-transform: uppercase; font-size: 1rem; letter-spacing: 2px; color: rgba(240, 236, 228, 0.5); margin: 0;">Instrument</h5>
                            <p style="font-size: 2rem; font-family: var(--font-heading); font-weight: bold; color: var(--cream); margin: 0; line-height: 1;">SAFE (€1M)</p>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1px solid rgba(242,237,228,0.1); padding-bottom: 1rem;">
                            <h5 style="text-transform: uppercase; font-size: 1rem; letter-spacing: 2px; color: rgba(240, 236, 228, 0.5); margin: 0;">Valuation Cap</h5>
                            <p style="font-size: 2rem; font-family: var(--font-heading); font-weight: bold; color: var(--cream); margin: 0; line-height: 1;">€10M</p>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1px solid rgba(242,237,228,0.1); padding-bottom: 1rem;">
                            <h5 style="text-transform: uppercase; font-size: 1rem; letter-spacing: 2px; color: rgba(240, 236, 228, 0.5); margin: 0;">Allocation</h5>
                            <p style="font-size: 2rem; font-family: var(--font-heading); font-weight: bold; color: var(--cream); margin: 0; line-height: 1;">Max 2 Tickets</p>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1px solid rgba(242,237,228,0.1); padding-bottom: 1rem;">
                            <h5 style="text-transform: uppercase; font-size: 1rem; letter-spacing: 2px; color: rgba(240, 236, 228, 0.5); margin: 0;">Structure</h5>
                            <p style="font-size: 2rem; font-family: var(--font-heading); font-weight: bold; color: var(--cream); margin: 0; line-height: 1;">BV or INC</p>
                        </div>
                    </div>
                </div>
            </div>
            <a href="mailto:hello@buzbo.com" class="btn btn-primary" style="font-size: 1.25rem; padding: 1.25rem 3rem; width: 100%; text-align: center; display: block; box-sizing: border-box; margin-top: 4rem;">CLAIM A TICKET &rarr;</a>
        </div>
    </section>"""
content = content.replace(ask_old, ask_new)

# 3. Update FAQ section
faq_start_idx = content.find('<div class="faq-list">')
faq_end_idx = content.find('</div>\n        </div>\n    </section>\n\n    <!-- 10. Closing CTA -->')
faq_end_idx = content.find('</div>\n        </div>', faq_start_idx)

faq_new = """<div class="faq-list">
                
            <div class="faq-item">
                <button class="faq-question">What problem does Buzbo solve? <span>+</span></button>
                <div class="faq-answer">
                    <p style="font-weight:bold; margin-bottom:0.5rem; color:var(--cream);">Work changed. Hiring didn't.</p>
                    <p>AI has made hard skills a commodity. What actually determines success — how you communicate, what drives you, how you work with others — is still invisible in the hiring process.</p>
                    <p>Professionals are open to new opportunities but stuck: send a cold application, wait weeks, get rejected by an algorithm that never saw who they actually are.</p>
                    <p>Business managers want culture fit and the right energy. But the system gives them keyword-matched CVs filtered by HR.</p>
                    <p>Buzbo fixes this. Professionals build a human-first profile — values, work style, ambitions. Managers do the same. Both sides opt in before any conversation starts. No cold applications. No recruiters in between. Just the right people finding each other.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Why now? <span>+</span></button>
                <div class="faq-answer">
                    <p>AI removed hard-skill scarcity. What remains irreplaceable is who you are — how you communicate, what drives you, how you work.</p>
                    <p>The gap between what managers actually want and what the CV-based system delivers has never been wider. That gap is Buzbo's market.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Is this a tech company or an events company? <span>+</span></button>
                <div class="faq-answer">
                    <p style="font-weight:bold; margin-bottom:0.5rem; color:var(--cream);">Events are one of the channels. Software is the scale.</p>
                    <p>Events are a powerful tool to build the community, get people on the app and create organic trust. The app turns that trust into profiles, matches and paid users.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Is this LinkedIn with events? <span>+</span></button>
                <div class="faq-answer">
                    <p>LinkedIn is a directory — you share your feed and updates. Buzbo is how you expand your network: it actively connects people based on values, work style and culture fit.</p>
                    <p>LinkedIn is profile-first, reactive and search-driven. Buzbo is match-first and community-led.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Is this Bumble for jobs? <span>+</span></button>
                <div class="faq-answer">
                    <p>The mechanic is similar — both sides opt in, identity leads. But the category is more valuable.</p>
                    <p>Work has higher intent, longer relationships and stronger willingness to pay. This is a fundamentally larger market than dating.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">What proof do you have? <span>+</span></button>
                <div class="faq-answer">
                    <p style="font-weight:bold; margin-bottom:0.5rem; color:var(--cream);">Events:</p>
                    <ul>
                        <li>First Buzbo event, April 30 — 130 registrations, 70 attendees. Target was 50.</li>
                        <li>Event 2, June 4 — 20 paid registrations and growing.</li>
                    </ul>
                    <p style="font-weight:bold; margin-top:1rem; margin-bottom:0.5rem; color:var(--cream);">Community:</p>
                    <ul>
                        <li>260 total across waitlist and co-build</li>
                        <li>20 active investor conversations</li>
                        <li>10-person team, bootstrapped</li>
                    </ul>
                    <p style="margin-top:1rem;">Next proof: app launch, matching, first paid users.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Who pays first? <span>+</span></button>
                <div class="faq-answer">
                    <p>Buzbo equalizes the labour market: app subscriptions and pay-as-you-go for professionals. B2B access — companies, HR accounts — activates once the professional network reaches sufficient density.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">What's the €2.25M ARR scenario? <span>+</span></button>
                <div class="faq-answer">
                    <ul>
                        <li>100,000 users</li>
                        <li>7.5% paid conversion → 7,500 paid users</li>
                        <li>€250/year average → €2.25M ARR</li>
                    </ul>
                    <p style="margin-top:1rem;">This round tests the assumptions behind that model. The numbers are benchmarked against Bumble's early conversion data.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Why can this become venture-scale? <span>+</span></button>
                <div class="faq-answer">
                    <p>LinkedIn proved the scale of professional networks. Bumble proved identity-led matching can become a large paid platform.</p>
                    <p>Buzbo brings soft-skill matching, community, events and AI into one layer that neither has built. New category, not a feature.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">What makes this defensible? <span>+</span></button>
                <div class="faq-answer">
                    <p>The moat is not the software. It's the community and the brand.</p>
                    <p>City-by-city density is defensible. Trust, brand, local culture and matching history compound over time. A competitor can't replicate that with a feature launch.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Why this team? <span>+</span></button>
                <div class="faq-answer">
                    <ul>
                        <li><strong>Anouk (CEO):</strong> top-sport mentality, serial entrepreneur, ambitious leader.</li>
                        <li><strong>Elmer (CTO):</strong> senior engineer, architecture built to scale.</li>
                        <li><strong>Shinead (Growth Manager):</strong> owns community strategy, events and social.</li>
                        <li>Plus 7 contributors building on belief, mostly deferred compensation.</li>
                    </ul>
                    <p style="margin-top:1rem;">In their minds, the IPO is already a fact — now it's just execution. Capital will not create the momentum. It will accelerate what's already moving.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">What does this round prove? <span>+</span></button>
                <div class="faq-answer">
                    <ul>
                        <li>App launch</li>
                        <li>First paid conversion</li>
                        <li>Event-to-app acquisition</li>
                        <li>City-by-city expansion: NL → Germany → UK</li>
                        <li>Early B2B demand</li>
                    </ul>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Use of funds? <span>+</span></button>
                <div class="faq-answer">
                    <ul>
                        <li>App development</li>
                        <li>Events (NL, Germany, UK)</li>
                        <li>Team compensation</li>
                        <li>Growth and community</li>
                        <li>AI and matching infrastructure</li>
                        <li>Legal and entity setup</li>
                    </ul>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Why a convertible / SAFE? <span>+</span></button>
                <div class="faq-answer">
                    <p>We're early and moving fast. A convertible keeps the round simple, avoids a premature valuation debate, and lets strategic investors in before the next priced round. The next round will be used to expand into the US.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Legal structure? <span>+</span></button>
                <div class="faq-answer">
                    <p>Currently AH Limited B.V. A Buzbo B.V. will be incorporated at funding close. IP ownership and founder agreements are documented. A US entity (Delaware) will be evaluated if US investors participate.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Why USA? <span>+</span></button>
                <div class="faq-answer">
                    <p>The USA is the expansion market, not the starting point. We prove repeatable city density in NL, Germany and UK first — make mistakes fast, learn fast. New York is the target: the highest-density professional networking market in the world.</p>
                </div>
            </div>

            <div class="faq-item">
                <button class="faq-question">What should investors believe after reading this? <span>+</span></button>
                <div class="faq-answer">
                    <p style="font-weight:bold; margin-bottom:0.5rem; color:var(--cream);">Buzbo is early. But it is not theoretical.</p>
                    <p>130 people at the first event. A team building on belief. 20 active investor conversations. A clear path to city-by-city scale.</p>
                    <p>This is not another app. It's a new professional network built around who people are.</p>
                </div>
            </div>
"""

content = content[:faq_start_idx] + faq_new + content[faq_end_idx:]

with open("index.html", "w") as f:
    f.write(content)

