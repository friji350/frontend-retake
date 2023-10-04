<script lang="ts">
	/** @type {import('./$types').PageData} */
	export let data: import('./$types').PageData;

	let name = '';
	let description = '';
	let type = '';
	let img = '';

	import '../../global.css';
    import Header from '../../components/header/Header.svelte';
	import Footer from '../../components/footer/Footer.svelte';
	import AdminProjectCard from '../../components/adminItem/adminItem.svelte';

	function getCookie(cookieName) {
		const name = `${cookieName}=`;
		if (document.cookie) {
			const decodedCookie = decodeURIComponent(document.cookie);
			const cookieArray = decodedCookie.split(';');

			for (let i = 0; i < cookieArray.length; i++) {
				let cookie = cookieArray[i];
				while (cookie.charAt(0) === ' ') {
					cookie = cookie.substring(1);
				}
				if (cookie.indexOf(name) === 0) {
					return cookie.substring(name.length, cookie.length);
				}
			}
		}

		return null;
	}

	const addItem = async () => {
		const errorNameElement = document.getElementById('errorNameText') as HTMLElement;
		const errorDesElement = document.getElementById('errorDesText') as HTMLElement;

		if (name.length < 3) {
			errorNameElement.style.display = 'block';
			return;
		} else {
			errorNameElement.style.display = 'none';
		}

		if (description.length < 3) {
			errorDesElement.style.display = 'block';
			return;
		}  else {
			errorDesElement.style.display = 'none';
		}

		if (checkLinkValidity(img)) {
			const bearerToken = getCookie('token');

			const newItem = {
				name,
				type,
				img,
				description			
			};

			const response = await fetch('http://127.0.0.1:8000/api/add', {
				method: 'POST',
				headers: {
					Authorization: `Bearer ${bearerToken}`,
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ item: newItem, token: bearerToken })
			});

			if (response.ok) {
				const responseData = await response.json();
				console.log('Item created:', responseData);

				name = '';
				description = '';
				type = '';
				img = '';

				window.location.reload();
			} else {
				console.error('Error creating item');
			}
		}
	};

	function checkLinkValidity(url: string): boolean {
        const errorElement = document.getElementById('errorEmailText') as HTMLElement;
        // const url = inputElement.value.trim();
        const urlPattern = /^(ftp|http|https):\/\/[^ "]+$/;

        if (url === '' || url.match(urlPattern)) {
            errorElement.style.display = 'none';
            return true;
        } else {
            errorElement.style.display = 'block';
            return false;
        }
    }
</script>

<svelte:head>
    <title>{data.post?.titlePage}</title>
	<meta name="author" content={data.post?.author}>
	<meta name="description" content={data.post?.des}>
</svelte:head>

<Header />

<section class="profile">
	<form class="add_form">
		<label for="title">Title:</label>
		<input type="text" id="title" bind:value={name} />
	
		<label for="description">Description:</label>
		<textarea id="description" bind:value={description} />

		<label for="type">Type:</label>
		<textarea id="type" bind:value={type} />
	
		<label for="img">Image URL:</label>
		<input type="text" id="img" bind:value={img} />

		<span class="errorText" id="errorEmailText">The provided link is not valid. Please check and try again.</span>
		<span class="errorText" id="errorNameText">The project name should be at least 3 characters long.</span>
		<span class="errorText" id="errorDesText">The project description should be at least 3 characters long.</span>
	
		<button class="button" on:click={addItem}>Add Item</button>
	</form>

	<div class="project_list_cards">
		{#each data.post.itemCards as item}
			<AdminProjectCard 
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

<style>
	.add_form {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		flex-wrap: nowrap;
		gap: 5px;
	}

	.add_form label {
		color: #ffffff;
		font-family: 'Montserrat', sans-serif;
	}

	

	.add_form input, textarea {
		width: 300px;
	}

	.errorText {
		color: #c71313;
		font-family: 'Montserrat', sans-serif;
		display: none;
	}

</style>