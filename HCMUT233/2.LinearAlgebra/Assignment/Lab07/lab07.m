% Clear the workspace
clear;

% Load user_movies.mat file
load('users_movies.mat', 'movies', 'users_movies', 'users_movies_sort', 'index_small', 'trial_user');

% Get the dimensions
[m, n] = size(users_movies);

% Print a header indicating the movies to be listed
fprintf('Rating is based on the following %d most popular movies:\n', length(index_small));

% Loop through of the popular movies
for j = 1:length(index_small)
    % Print the movie title corresponding to the current index
    fprintf('%d. %s\n', j, movies{index_small(j)});
end

fprintf('\n');

% Select the users to compare to
[m1,n1]=size(users_movies_sort);
ratings=[];
for j=1:m1
    if prod(users_movies_sort(j,:))~=0
        ratings=[ratings; users_movies_sort(j,:)];
    end;
end;

% Find the Euclidean distances
[m2,n2]=size(ratings);
for i=1:m2
    eucl(i)=norm(ratings(i,:)-trial_user);
end;

% Find the smallest Euclidean distances
[smallest_number, position] = min(eucl);
disp(['Smallest Eucl: ', num2str(smallest_number)]);
disp(['Position: ', num2str(position)]);

% Compute the Pearson correlation coefficient
pearson = zeros(size(ratings, 1), 1);
trial_user = trial_user(:)';

% Compute correlation along the ratings vectors
for i=1:size(ratings,1)
    current_rating = ratings(i, :);

    % Compute mean
    trial_user_mean = mean(trial_user);
    current_ratings_mean = mean(current_rating);

    % Subtract with the mean
    trial_user_centered = trial_user - trial_user_mean;
    current_ratings_centered = current_rating - current_ratings_mean;
    
    pearson_numerator = sum(trial_user_centered .* current_ratings_centered);
    pearson_denominator = sqrt(sum(trial_user_centered .^2) .* sum(current_ratings_centered .^2));
    if pearson_denominator ~= 0
        corr = pearson_numerator / pearson_denominator;
    else
        corr = 0;
    end;
    pearson(i) = corr;
end;

% Find the highest Pearson correlation coefficient
[max_pearson, pearson_index] = max(pearson);
disp(['Highest Pearson correlation coefficient: ', num2str(max_pearson)]);
disp(['Position: ', num2str(pearson_index)]);
