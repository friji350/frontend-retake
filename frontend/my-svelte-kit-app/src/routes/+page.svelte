<script>
    import '../global.css';
    import Header from '../components/header/Header.svelte';
    import Footer from '../components/footer/Footer.svelte';
    import ProjectCard from '../components/projectCard/projectCard.svelte';
</script>

<svelte:head>
    <title>Home</title>
	<meta name="author" content="Anton Fadeenkov">
	<meta name="description" content="Home Page">
</svelte:head>

<Header />

<main>
    <section class="hero" id="hero">
        <div class="hero_top" id="header_top">
            <div class="h_back_fix">
                <h1>
                    <span class="background_h">
                        Digital Agency
                    </span>
                </h1>
                <h1>
                    <span>focused on the Internet</span>
                </h1>
            </div>
            <p>
                We are a creative team of designers, developers, strategists and producers creating high-quality websites
            </p>
            <a href="/" class="button">Order a project</a>
        </div>
        <div class="nothing_block"></div>
    </section>

    <section class="our_plus">
        <div class="h_back_fix">
            <h1>
                    <span class="background_h">
                        But what does it give
                    </span>
            </h1>
            <h1>
                <span> your business?</span>
            </h1>
        </div>


        <div class="plus_cards_list">
            <div class="plus_card">
                <img alt="plus_svg_1" src="/01.svg" class="plus_card_number">
                <div class="plus_line_card"></div>
                <p class="plus_card_text">
                    Presentation of a company with a BOOM effect
                </p>
            </div>
            <div class="plus_card">
                <img alt="plus_svg_2" src="/02.svg" class="plus_card_number">
                <div class="plus_line_card"></div>
                <p class="plus_card_text">
                    Brand image support and enhancement
                </p>
            </div>
            <div class="plus_card">
                <img alt="plus_svg_3" src="/03.svg" class="plus_card_number">
                <div class="plus_line_card"></div>
                <p class="plus_card_text">
                    Increase sales by increasing conversions
                </p>
            </div>
        </div>
    </section>

    <section class="profile">
        <h3 class="title">
            And now our projects
        </h3>

        <div class="project_list_cards">
                    
            <ProjectCard 
                id={13}
                name={"DROOPY"}
                type={"Branding"}
                description={"EXPRESS DELIVERY COMPANY"}
                img={"https://i.postimg.cc/L89vdFGm/droopy.png"}
            />

            <ProjectCard 
                id={11}
                name={"AVANTI"}
                type={"UI/UX Design"}
                description={"COMMERCIAL LIGHTING"}
                img={"https://i.postimg.cc/xCWRZvYK/Avanti.png"}
            />
        </div>
        <a href="/catalog" class="button w100 mt50px">View all</a>
    </section>
    <section class="back_form">
        <div class="h_back_fix">
            <h1>
                    <span class="background_h">
                        Let's start making 
                    </span>
            </h1>
            <h1>
                <span>your business better!</span>
            </h1>
        </div>
        <form>
            <input type="text" name="fio" id="fio" class="form_text_input" placeholder="FCs">
            <input type="text" name="email" id="email" class="form_text_input" placeholder="Mail">
            <input type="text" name="idea" id="idea" class="form_text_input" placeholder="Idea">
            <button type="submit" class="button">Send</button>
        </form>
    </section>
</main>

<Footer />