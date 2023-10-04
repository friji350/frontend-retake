<script lang="ts">
    export let id: number;
    export let name: string;
    export let type: string;
    export let description: string;
    export let img: string;
</script>

<a href={`/item?id=${id}`}  class="project_card">
    <div style="background-image: url({img});" class="project_card_image">
        <span class="project_card_info">{type}</span>
    </div>
    <span class="project_card_description">
        <span class="project_card_name">{name} - </span>
        {description}
    </span>
</a>
