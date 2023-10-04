<script lang="ts">
    import {_deleteItem} from "../../routes/admin/+page.ts";

    export let id: number;
    export let name: string;
    export let type: string;
    export let description: string;
    export let img: string;

    function handleAddButtonKeydown(event: KeyboardEvent) {
    if (event.key === 'Enter') {
        handleAddButtonClick();
    }
    }

    function handleAddButtonClick() {
        _deleteItem({id});
    }

</script>

<div  class="project_card">
    <div style="background-image: url({img});" class="project_card_image">
        <span class="project_card_info">{type}</span>
    </div>
    <span class="project_card_description">
        <span class="project_card_name">{name} - </span>
        {description}
    </span>
    <button class="button" on:click={handleAddButtonClick} on:keydown={handleAddButtonKeydown}>Delete</button>
</div>


<style>
    .button:hover{
        cursor: pointer;
    }
    .button{
        background-color: red;
    }
</style>