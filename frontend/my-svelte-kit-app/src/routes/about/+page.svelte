<script lang="ts">
    export let data;
	import '../../global.css';
    import Header from '../../components/header/Header.svelte';
	import Footer from '../../components/footer/Footer.svelte';
</script>

<svelte:head>
    <title>{data.post.titlePage}</title>
	<meta name="author" content={data.post.author}>
	<meta name="description" content={data.post.des}>
</svelte:head>

<Header />

<section class="aboutUs">
	<h2>AxelDev: Your Digital Agency for Websites, Branding, and Design</h2>
    <section>
        <h2>Our Services:</h2>
        <ol>
            <li>
                <h3>Website Development</h3>
                <p>At AxelDev, we specialize in creating visually appealing and functionally robust websites tailored to your needs.</p>
            </li>
            <li>
                <h3>Branding</h3>
                <p>We craft memorable brand strategies, logos, and messaging that resonate with your audience and set you apart.</p>
            </li>
            <li>
                <h3>Design</h3>
                <p>Our creative team turns ideas into visually stunning concepts, from UI/UX design to print materials.</p>
            </li>
        </ol>
    </section>
    <section>
        <h2>Why Choose AxelDev:</h2>
        <ul>
            <li><p>Expertise: Our team of professionals stays up-to-date with industry trends and technologies.</p></li>
            <li><p>Customization: We offer tailor-made solutions to meet your unique requirements and goals.</p></li>
            <li><p>Collaboration: We believe in open communication and collaboration throughout the project.</p></li>
            <li><p>Quality Assurance: Rigorous testing ensures the highest quality in every project.</p></li>
            <li><p>Timely Delivery: We value your time and deliver projects on time and within budget.</p></li>
            <li><p>Client-Centric Approach: Your success is our success; we build long-term relationships and provide ongoing support.</p></li>
        </ul>
    </section>
    <section>
        <p>At AxelDev, we don't just create websites, brands, and designs; we craft digital experiences that captivate, engage, and inspire. Whether you're a startup looking to establish your online presence, a growing business seeking to rebrand, or an individual with a creative vision, AxelDev is your trusted partner in the digital realm. Let's embark on a journey of creativity and innovation together. <a href="mailto:info@axeldev.com">Contact us today</a> to get started.</p>
    </section>
</section>

<Footer />

<style>
	.aboutUs {
		width: 100%;
		max-width: 1290px;
		margin-left: auto;
		margin-right: auto;
		padding-top: 200px;
		margin-bottom: 200px;
		font-family: 'Montserrat', sans-serif;
	}

	
</style>