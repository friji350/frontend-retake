<!-- src/routes/item/[itemId].svelte -->

<script lang="ts">
	/** @type {import('./$types').PageData} */
	export let data: import('./$types').PageData;
	import Header from '../../components/header/Header.svelte';
	import Footer from '../../components/footer/Footer.svelte';
	import '../../global.css';
  </script>
  
  <svelte:head>
    <title>{data.post?.titlePage}</title>
	<meta name="author" content={data.post?.author}>
	<meta name="description" content={data.post?.des}>
</svelte:head>

  <Header />
  
  <section class="itemHero">
	<div class="mainInfo">
	  <h1>{data.post.itemCard.name}</h1>
	  <span>{data.post.itemCard.description}</span>
	  <a class="button" href="/catalog">View all catalog</a>
	</div>
	<img src='{data.post.itemCard.img}' alt='' />
  </section>
  
  <Footer />
  
  <style>
	.itemHero {
	  max-width: 1290px;
	  width: 100%;
	  height: 90vh;
	  margin-left: auto;
	  margin-right: auto;
	  display: flex;
	  flex-direction: row;
	  align-items: center;
	  justify-content: space-between;
	  align-content: center;
	}
	.itemHero img {
	  max-width: 550px;
	}
  
	.mainInfo {
	  display: flex;
	  flex-direction: column;
	  align-items: flex-start;
	  align-content: flex-start;
	  flex-wrap: nowrap;
	  gap: 20px;
	}
  
	@media (max-width: 850px) {
	  .itemHero  {
		flex-direction: column;
		justify-content: center;
		gap: 50px;
	  }
	}
  </style>
  