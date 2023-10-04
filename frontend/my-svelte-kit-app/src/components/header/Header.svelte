<style>
    header {
        background-color: #151515;
        position: fixed;
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        align-content: center;
        align-items: center;
        justify-content: space-between;
        color: #ffffff;
        width: 100%;
        padding-left: calc((100% - 1290px) / 2);
        padding-right: calc((100% - 1290px) / 2);
        z-index: 99999999999;
    }

    ul {
        display: flex;
        gap: 25px;
        
    }

    header a{
        font-size: 16px;
    }

    header h1 {
        font-size: 24px;
        color: #ffffff;
    }

    @media (max-width: 600px) {
    header h1 {
        font-size: 16px !important;
    }
  }

</style>

<header>
    <h1>AxelDev</h1>
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About us</a></li>
        <li><a href="/catalog">Catalog</a></li>
      </ul>
    </nav>
</header>