<script lang="ts">
	/** @type {import('./$types').PageData} */
	export let data: import('./$types').PageData;

	import '../../global.css';
    import Header from '../../components/header/Header.svelte';
	import Footer from '../../components/footer/Footer.svelte';
	import ProjectCard from '../../components/projectCard/projectCard.svelte';
</script>

<svelte:head>
    <title>{data.post?.titlePage}</title>
	<meta name="author" content={data.post?.author}>
	<meta name="description" content={data.post?.des}>
</svelte:head>

<Header />

<section class="profile">
	<h3 class="title">
		And now our projects
	</h3>

	<div class="project_list_cards">
		{#each data.post.itemCards as item}
			<ProjectCard 
				id={item.id}
				name={item.name}
				type={item.type}
				description={item.description}
				img={item.img}
			/>
        {/each}	
		
	</div>
</section>


<Footer />