import React, { useState, useEffect } from 'react';
import ProductCard from './ProductCard';
import { getProducts } from './api';

function AllProducts() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      setLoading(true);
      const data = await getProducts();
      setProducts(data.products);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching products:', error);
      setLoading(false);
    }
  };

  return (
    <div>
      {loading ? (
        <div>Loading...</div>
      ) : (
        <>
          {}
          {products.map(product => (
            <ProductCard key={product.id} product={product} />
          ))}
          {}
          <button onClick={fetchProducts}>Refresh Products</button>
        </>
      )}
    </div>
  );
}

export default AllProducts;