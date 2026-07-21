/* ==========================================
   NeuralRetail - SAAS Dashboard Logic & Visualizations
   Chart.js, AOS, Interactive Simulators & Counters
   ========================================== */

document.addEventListener('DOMContentLoaded', () => {
  // Initialize AOS (Animate On Scroll)
  if (typeof AOS !== 'undefined') {
    AOS.init({
      duration: 800,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }

  // 1. Dark / Light Theme Switcher
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  const themeIcon = document.getElementById('themeIcon');
  
  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme');
      if (currentTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'dark');
        themeIcon.className = 'fas fa-moon';
        localStorage.setItem('theme', 'dark');
      } else {
        document.documentElement.setAttribute('data-theme', 'light');
        themeIcon.className = 'fas fa-sun';
        localStorage.setItem('theme', 'light');
      }
    });

    // Check saved preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      document.documentElement.setAttribute('data-theme', savedTheme);
      themeIcon.className = savedTheme === 'light' ? 'fas fa-sun' : 'fas fa-moon';
    }
  }

  // 2. Back To Top Button
  const backToTopBtn = document.getElementById('backToTopBtn');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      backToTopBtn?.classList.add('show');
    } else {
      backToTopBtn?.classList.remove('show');
    }
  });

  backToTopBtn?.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // 3. Animated Stat Counters
  const counterElements = document.querySelectorAll('.counter');
  let animated = false;

  const animateCounters = () => {
    counterElements.forEach(counter => {
      const target = +counter.getAttribute('data-target');
      const suffix = counter.getAttribute('data-suffix') || '';
      const decimals = +counter.getAttribute('data-decimals') || 0;
      let count = 0;
      const speed = target / 60;

      const updateCount = () => {
        count += speed;
        if (count < target) {
          counter.innerText = count.toFixed(decimals) + suffix;
          setTimeout(updateCount, 25);
        } else {
          counter.innerText = target.toFixed(decimals) + suffix;
        }
      };
      updateCount();
    });
  };

  // Intersection Observer for Counters
  const counterSection = document.getElementById('stats-section');
  if (counterSection) {
    const observer = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting && !animated) {
        animateCounters();
        animated = true;
      }
    }, { threshold: 0.3 });
    observer.observe(counterSection);
  }

  // ==========================================
  // CHART.JS INITIALIZATIONS
  // ==========================================

  // Chart Global Styling Overrides for Dark SaaS Aesthetics
  Chart.defaults.color = '#94a3b8';
  Chart.defaults.font.family = "'Inter', sans-serif";
  Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.08)';

  // ------------------------------------------
  // A. Demand Forecasting Chart
  // ------------------------------------------
  const forecastCtx = document.getElementById('forecastChart')?.getContext('2d');
  let forecastChart;

  if (forecastCtx) {
    const dates = ['Jan 1', 'Jan 5', 'Jan 10', 'Jan 15', 'Jan 20', 'Jan 25', 'Jan 30', 'Feb 5', 'Feb 10', 'Feb 15', 'Feb 20', 'Feb 25', 'Mar 1'];
    const actualData = [1200, 1350, 1280, 1420, 1500, 1620, 1580, 1710, 1800, 1750, 1890, 1950, 2050];
    const ensembleData = [1210, 1340, 1290, 1410, 1515, 1610, 1595, 1700, 1810, 1760, 1880, 1960, 2040];
    const prophetData = [1180, 1320, 1270, 1450, 1490, 1580, 1610, 1680, 1790, 1720, 1850, 1920, 2010];
    const lstmData = [1225, 1365, 1310, 1400, 1530, 1635, 1570, 1725, 1825, 1780, 1905, 1980, 2070];
    const neuralProphetData = [1205, 1335, 1285, 1415, 1505, 1615, 1585, 1705, 1805, 1755, 1885, 1955, 2045];

    forecastChart = new Chart(forecastCtx, {
      type: 'line',
      data: {
        labels: dates,
        datasets: [
          {
            label: 'Actual Sales',
            data: actualData,
            borderColor: '#00f2fe',
            backgroundColor: 'rgba(0, 242, 254, 0.1)',
            borderWidth: 3,
            fill: true,
            tension: 0.35,
            pointRadius: 4
          },
          {
            label: 'Ensemble Model (Best)',
            data: ensembleData,
            borderColor: '#00f5d4',
            borderWidth: 2,
            borderDash: [5, 5],
            tension: 0.35,
            pointRadius: 2
          },
          {
            label: 'Prophet',
            data: prophetData,
            borderColor: '#7928ca',
            borderWidth: 2,
            tension: 0.35,
            hidden: true
          },
          {
            label: 'LSTM Deep Learning',
            data: lstmData,
            borderColor: '#ff007f',
            borderWidth: 2,
            tension: 0.35,
            hidden: true
          },
          {
            label: 'NeuralProphet',
            data: neuralProphetData,
            borderColor: '#f6d365',
            borderWidth: 2,
            tension: 0.35,
            hidden: true
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'top',
            labels: { boxWidth: 12, usePointStyle: true, font: { weight: '600' } }
          },
          tooltip: {
            mode: 'index',
            intersect: false,
            backgroundColor: '#0d121f',
            titleColor: '#00f2fe',
            borderColor: 'rgba(0,242,254,0.3)',
            borderWidth: 1
          }
        },
        scales: {
          x: { grid: { color: 'rgba(255, 255, 255, 0.05)' } },
          y: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, title: { display: true, text: 'Demand (Units / Day)' } }
        }
      }
    });

    // Model Filter Buttons
    document.querySelectorAll('.forecast-model-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        document.querySelectorAll('.forecast-model-btn').forEach(b => b.classList.remove('btn-gradient-primary'));
        document.querySelectorAll('.forecast-model-btn').forEach(b => b.classList.add('btn-glass-secondary'));
        btn.classList.remove('btn-glass-secondary');
        btn.classList.add('btn-gradient-primary');

        const model = btn.getAttribute('data-model');
        forecastChart.data.datasets.forEach((ds, idx) => {
          if (model === 'all') {
            ds.hidden = false;
          } else if (model === 'ensemble' && (idx === 0 || idx === 1)) {
            ds.hidden = false;
          } else if (model === 'prophet' && (idx === 0 || idx === 2)) {
            ds.hidden = false;
          } else if (model === 'lstm' && (idx === 0 || idx === 3)) {
            ds.hidden = false;
          } else if (model === 'neuralprophet' && (idx === 0 || idx === 4)) {
            ds.hidden = false;
          } else {
            ds.hidden = true;
          }
        });
        forecastChart.update();
      });
    });
  }

  // ------------------------------------------
  // B. Churn Prediction - ROC Curve & SHAP
  // ------------------------------------------
  const rocCtx = document.getElementById('rocChart')?.getContext('2d');
  if (rocCtx) {
    new Chart(rocCtx, {
      type: 'line',
      data: {
        labels: [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        datasets: [
          {
            label: 'XGBoost Churn Classifier (AUC = 0.94)',
            data: [0.0, 0.45, 0.72, 0.84, 0.90, 0.94, 0.96, 0.98, 0.99, 1.0, 1.0],
            borderColor: '#00f5d4',
            backgroundColor: 'rgba(0, 245, 212, 0.12)',
            fill: true,
            borderWidth: 3,
            tension: 0.2
          },
          {
            label: 'Random Baseline (AUC = 0.50)',
            data: [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
            borderColor: '#64748b',
            borderDash: [6, 6],
            borderWidth: 2
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { position: 'top' }
        },
        scales: {
          x: { title: { display: true, text: 'False Positive Rate (1 - Specificity)' } },
          y: { title: { display: true, text: 'True Positive Rate (Sensitivity)' } }
        }
      }
    });
  }

  // SHAP Feature Importance Chart
  const shapCtx = document.getElementById('shapChart')?.getContext('2d');
  if (shapCtx) {
    new Chart(shapCtx, {
      type: 'bar',
      data: {
        labels: ['Recency (Days Inactive)', 'Avg Order Value ($)', 'Discount Usage Rate', 'Support Tickets', 'Purchase Frequency', 'Cart Abandonment Rate'],
        datasets: [{
          label: 'SHAP Feature Importance Value',
          data: [0.38, 0.27, 0.19, 0.14, 0.11, 0.08],
          backgroundColor: [
            '#00f2fe', '#4facfe', '#7928ca', '#ff007f', '#00f5d4', '#f6d365'
          ],
          borderRadius: 6
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          x: { title: { display: true, text: 'Mean |SHAP Value| (Impact on Model Outcome)' } }
        }
      }
    });
  }

  // ------------------------------------------
  // C. Customer Segmentation RFM Scatter & Pie
  // ------------------------------------------
  const segPieCtx = document.getElementById('segmentPieChart')?.getContext('2d');
  if (segPieCtx) {
    new Chart(segPieCtx, {
      type: 'doughnut',
      data: {
        labels: ['Champions (High RFM)', 'Loyal Customers', 'At-Risk / Lapsing', 'Lost / Inactive'],
        datasets: [{
          data: [28, 36, 22, 14],
          backgroundColor: ['#00f5d4', '#00f2fe', '#f6d365', '#ff416c'],
          borderWidth: 2,
          borderColor: '#0d121f'
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { position: 'bottom' }
        },
        cutout: '70%'
      }
    });
  }

  const rfmScatterCtx = document.getElementById('rfmScatterChart')?.getContext('2d');
  if (rfmScatterCtx) {
    new Chart(rfmScatterCtx, {
      type: 'scatter',
      data: {
        datasets: [
          {
            label: 'Champions',
            data: [{x: 5, y: 950}, {x: 8, y: 1200}, {x: 12, y: 880}, {x: 15, y: 1400}, {x: 10, y: 1100}],
            backgroundColor: '#00f5d4'
          },
          {
            label: 'Loyal Customers',
            data: [{x: 25, y: 650}, {x: 30, y: 720}, {x: 35, y: 580}, {x: 40, y: 800}],
            backgroundColor: '#00f2fe'
          },
          {
            label: 'At-Risk',
            data: [{x: 65, y: 350}, {x: 75, y: 420}, {x: 80, y: 290}, {x: 90, y: 310}],
            backgroundColor: '#f6d365'
          },
          {
            label: 'Lost',
            data: [{x: 120, y: 90}, {x: 140, y: 110}, {x: 160, y: 85}, {x: 180, y: 60}],
            backgroundColor: '#ff416c'
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: { title: { display: true, text: 'Recency (Days Since Last Order)' } },
          y: { title: { display: true, text: 'Monetary Value ($ Annual Spend)' } }
        }
      }
    });
  }

  // ------------------------------------------
  // D. Price Elasticity & Dynamic Revenue Simulator
  // ------------------------------------------
  const priceCtx = document.getElementById('priceElasticityChart')?.getContext('2d');
  let priceChart;

  const prices = [10, 15, 20, 25, 30, 35, 40, 45, 50];
  // Price elasticity model Q = 1000 - 18.5 * Price
  const demands = prices.map(p => Math.max(50, Math.round(1200 - 22 * p)));
  const revenues = prices.map((p, idx) => p * demands[idx]);

  if (priceCtx) {
    priceChart = new Chart(priceCtx, {
      type: 'line',
      data: {
        labels: prices.map(p => `$${p}`),
        datasets: [
          {
            label: 'Predicted Demand (Units)',
            data: demands,
            borderColor: '#00f2fe',
            yAxisID: 'y',
            tension: 0.3
          },
          {
            label: 'Projected Total Revenue ($)',
            data: revenues,
            borderColor: '#00f5d4',
            backgroundColor: 'rgba(0, 245, 212, 0.1)',
            fill: true,
            yAxisID: 'y1',
            tension: 0.3
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: { title: { display: true, text: 'Product Unit Price ($)' } },
          y: { type: 'linear', position: 'left', title: { display: true, text: 'Demand (Units)' } },
          y1: { type: 'linear', position: 'right', grid: { drawOnChartArea: false }, title: { display: true, text: 'Revenue ($)' } }
        }
      }
    });
  }

  // Dynamic Revenue Calculator Slider
  const priceSlider = document.getElementById('priceSlider');
  const priceVal = document.getElementById('calcPriceVal');
  const demandVal = document.getElementById('calcDemandVal');
  const revenueVal = document.getElementById('calcRevenueVal');
  const marginVal = document.getElementById('calcMarginVal');

  if (priceSlider) {
    priceSlider.addEventListener('input', (e) => {
      const price = parseFloat(e.target.value);
      // Demand equation Q = 1200 - 22 * Price
      const estDemand = Math.max(20, Math.round(1200 - 22 * price));
      const estRevenue = price * estDemand;
      const unitCost = 12; // Base cost $12
      const profitMargin = (((price - unitCost) / price) * 100).toFixed(1);

      if (priceVal) priceVal.innerText = `$${price.toFixed(2)}`;
      if (demandVal) demandVal.innerText = `${estDemand.toLocaleString()} units`;
      if (revenueVal) revenueVal.innerText = `$${estRevenue.toLocaleString()}`;
      if (marginVal) marginVal.innerText = `${profitMargin}%`;
    });
  }

  // ------------------------------------------
  // E. Image Screenshot Preview Modal & Upload Placeholder Logic
  // ------------------------------------------
  const screenshotContainers = document.querySelectorAll('.screenshot-container');
  const imageModal = document.getElementById('imagePreviewModal');
  const modalImg = document.getElementById('modalImagePreview');
  const modalTitle = document.getElementById('modalImageTitle');
  const imageUploadInput = document.getElementById('globalImageUploader');

  let activePlaceholderCard = null;

  screenshotContainers.forEach(container => {
    container.addEventListener('click', () => {
      activePlaceholderCard = container;
      const existingImg = container.querySelector('img');
      const title = container.getAttribute('data-title') || 'Project Visual';

      if (existingImg && existingImg.src) {
        // Show Modal Zoom
        if (modalImg && modalTitle) {
          modalImg.src = existingImg.src;
          modalTitle.innerText = title;
          const bsModal = new bootstrap.Modal(imageModal);
          bsModal.show();
        }
      } else {
        // Trigger File Upload to customize graph screenshot
        imageUploadInput?.click();
      }
    });
  });

  // Handle Local File Upload Replacement
  imageUploadInput?.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file && activePlaceholderCard) {
      const reader = new FileReader();
      reader.onload = (evt) => {
        const imgUrl = evt.target.result;
        activePlaceholderCard.innerHTML = `<img src="${imgUrl}" class="img-preview" alt="Project Screenshot">`;
      };
      reader.readAsDataURL(file);
    }
  });

  // Gallery Filter Buttons
  const filterBtns = document.querySelectorAll('.gallery-filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-item');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active', 'btn-gradient-primary'));
      filterBtns.forEach(b => b.classList.add('btn-glass-secondary'));
      btn.classList.remove('btn-glass-secondary');
      btn.classList.add('active', 'btn-gradient-primary');

      const cat = btn.getAttribute('data-filter');

      galleryItems.forEach(item => {
        if (cat === 'all' || item.getAttribute('data-category') === cat) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });

});
