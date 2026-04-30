const menuButton = document.querySelector("[data-menu-button]");
const mobileMenu = document.querySelector("[data-mobile-menu]");

if (menuButton && mobileMenu) {
  menuButton.addEventListener("click", () => {
    mobileMenu.classList.toggle("hidden");
  });
}

document.querySelectorAll("img[data-fallback-src]").forEach((image) => {
  image.addEventListener(
    "error",
    () => {
      image.src = image.dataset.fallbackSrc;
      image.removeAttribute("data-fallback-src");
    },
    { once: true },
  );
});

document.querySelectorAll("[data-profile-slideshow]").forEach((slideshow) => {
  const slides = Array.from(slideshow.querySelectorAll(".profile-slide"));
  const thumbnails = Array.from(
    document.querySelectorAll("[data-profile-thumbnails] img"),
  );

  if (slides.length < 2) {
    return;
  }

  let activeIndex = slides.findIndex((slide) =>
    slide.classList.contains("profile-slide-active"),
  );

  if (activeIndex < 0) {
    activeIndex = 0;
    slides[activeIndex].classList.add("profile-slide-active");
  }

  const updateThumbnails = () => {
    thumbnails.forEach((thumbnail, thumbnailIndex) => {
      const slide = slides[(activeIndex + thumbnailIndex + 1) % slides.length];
      thumbnail.src = slide.currentSrc || slide.src;
      thumbnail.alt = slide.alt;
    });
  };

  updateThumbnails();

  setInterval(() => {
    slides[activeIndex].classList.remove("profile-slide-active");
    activeIndex = (activeIndex + 1) % slides.length;
    slides[activeIndex].classList.add("profile-slide-active");
    updateThumbnails();
  }, 2000);
});

const pingForm = document.querySelector("[data-ping-form]");

if (pingForm) {
  const pingButton = document.querySelector("[data-ping-button]");
  const errorBox = document.querySelector("[data-ping-error]");
  const packetAnalysis = document.querySelector("[data-packet-analysis]");
  const copyButton = document.querySelector("[data-copy-ping]");
  const resultFields = {
    target: document.querySelector("[data-result-target]"),
    loss: document.querySelector("[data-result-loss]"),
    avg: document.querySelector("[data-result-avg]"),
    min: document.querySelector("[data-result-min]"),
    max: document.querySelector("[data-result-max]"),
    packets: document.querySelector("[data-result-packets]"),
  };

  const formatLatency = (value) => (value === null ? "-" : `${value}ms`);

  const setError = (message) => {
    errorBox.textContent = message;
    errorBox.classList.remove("hidden");
  };

  const clearError = () => {
    errorBox.textContent = "";
    errorBox.classList.add("hidden");
  };

  pingForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    clearError();

    const formData = new FormData(pingForm);
    const target = formData.get("target").trim();

    if (!target) {
      setError("Enter an IP address or hostname first.");
      return;
    }

    pingButton.disabled = true;
    pingButton.textContent = "Pinging...";
    packetAnalysis.textContent = "Running diagnostic...";

    try {
      const response = await fetch(`/tools/ping/?target=${encodeURIComponent(target)}`);
      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Ping failed.");
      }

      resultFields.target.textContent = data.target;
      resultFields.loss.textContent = `${data.packet_loss}%`;
      resultFields.avg.textContent = formatLatency(data.avg_latency);
      resultFields.min.textContent = formatLatency(data.min_latency);
      resultFields.max.textContent = formatLatency(data.max_latency);
      resultFields.packets.textContent = `${data.packets.length}/4`;

      if (data.packets.length) {
        packetAnalysis.textContent = data.packets
          .map((packet) => `${packet.index}. OK  Time: ${packet.time}ms`)
          .join("\n");
      } else {
        packetAnalysis.textContent = "No packets returned. The target may be blocked or unreachable.";
      }
    } catch (error) {
      setError(error.message);
      packetAnalysis.textContent = "No results yet.";
    } finally {
      pingButton.disabled = false;
      pingButton.textContent = "Ping";
    }
  });

  copyButton.addEventListener("click", async () => {
    const summary = [
      `Target: ${resultFields.target.textContent}`,
      `Packet Loss: ${resultFields.loss.textContent}`,
      `Avg Latency: ${resultFields.avg.textContent}`,
      `Min Latency: ${resultFields.min.textContent}`,
      `Max Latency: ${resultFields.max.textContent}`,
      "",
      packetAnalysis.textContent,
    ].join("\n");

    await navigator.clipboard.writeText(summary);
    copyButton.textContent = "Copied";
    setTimeout(() => {
      copyButton.textContent = "Copy results";
    }, 1200);
  });
}
